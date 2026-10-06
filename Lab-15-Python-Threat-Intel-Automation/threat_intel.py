import os
import requests
import ipaddress
import json
import csv
from datetime import datetime


API_KEY = os.getenv("ABUSEIPDB_API_KEY")
API_URL = "https://api.abuseipdb.com/api/v2/check"


def validate_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)

        if (
            ip_obj.is_private
            or ip_obj.is_loopback
            or ip_obj.is_reserved
            or ip_obj.is_multicast
            or ip_obj.is_unspecified
        ):
            return False

        return True

    except ValueError:
        return False


def check_ip_reputation(ip):
    headers = {
        "Accept": "application/json",
        "Key": API_KEY
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90,
        "verbose": True
    }

    response = requests.get(
        API_URL,
        headers=headers,
        params=params,
        timeout=10
    )

    response.raise_for_status()
    return response.json()


def classify_risk(score):
    if score >= 75:
        return "HIGH"
    elif score >= 25:
        return "MEDIUM"
    else:
        return "LOW"


def get_recommended_action(risk_level):
    if risk_level == "HIGH":
        return "Escalate for analyst investigation"
    elif risk_level == "MEDIUM":
        return "Review additional context and investigate"
    else:
        return "Document and monitor"


def save_json_result(data, risk_level, recommended_action):
    output_data = {
        "timestamp": datetime.now().isoformat(),
        "ip_address": data["ipAddress"],
        "country": data.get("countryCode", "N/A"),
        "isp": data.get("isp", "N/A"),
        "domain": data.get("domain", "N/A"),
        "usage_type": data.get("usageType", "N/A"),
        "abuse_confidence_score": data["abuseConfidenceScore"],
        "total_reports": data.get("totalReports", 0),
        "last_reported": data.get("lastReportedAt", "N/A"),
        "risk_level": risk_level,
        "recommended_action": recommended_action
    }

    os.makedirs("output", exist_ok=True)

    safe_ip = data["ipAddress"].replace(":", "_")
    filename = f"output/{safe_ip}_report.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(output_data, file, indent=4)

    return filename


def save_csv_result(data, risk_level, recommended_action):
    os.makedirs("output", exist_ok=True)

    filename = "output/threat_intel_results.csv"
    file_exists = os.path.exists(filename)

    fieldnames = [
        "timestamp",
        "ip_address",
        "country",
        "isp",
        "domain",
        "usage_type",
        "abuse_confidence_score",
        "total_reports",
        "last_reported",
        "risk_level",
        "recommended_action"
    ]

    row = {
        "timestamp": datetime.now().isoformat(),
        "ip_address": data["ipAddress"],
        "country": data.get("countryCode", "N/A"),
        "isp": data.get("isp", "N/A"),
        "domain": data.get("domain", "N/A"),
        "usage_type": data.get("usageType", "N/A"),
        "abuse_confidence_score": data["abuseConfidenceScore"],
        "total_reports": data.get("totalReports", 0),
        "last_reported": data.get("lastReportedAt", "N/A"),
        "risk_level": risk_level,
        "recommended_action": recommended_action
    }

    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(row)

    return filename


def main():
    print("=== Threat Intelligence IP Checker ===")

    ip = input("Enter an IP address: ").strip()

    if not validate_ip(ip):
        print("Invalid, private, or reserved IP address.")
        return

    if not API_KEY:
        print("API key not found.")
        return

    try:
        result = check_ip_reputation(ip)
        data = result["data"]

        score = data["abuseConfidenceScore"]
        risk_level = classify_risk(score)
        recommended_action = get_recommended_action(risk_level)

        output_file = save_json_result(
            data,
            risk_level,
            recommended_action
        )

        csv_file = save_csv_result(
            data,
            risk_level,
            recommended_action
        )

        print("\n=== Threat Intelligence Result ===")
        print(f"IP Address: {data['ipAddress']}")
        print(f"Country: {data.get('countryCode', 'N/A')}")
        print(f"ISP: {data.get('isp', 'N/A')}")
        print(f"Domain: {data.get('domain', 'N/A')}")
        print(f"Usage Type: {data.get('usageType', 'N/A')}")
        print(f"Abuse Confidence Score: {score}")
        print(f"Total Reports: {data.get('totalReports', 0)}")
        print(f"Last Reported: {data.get('lastReportedAt', 'N/A')}")
        print(f"Risk Level: {risk_level}")
        print(f"Recommended Action: {recommended_action}")
        print(f"Report Saved: {output_file}")
        print(f"CSV Updated: {csv_file}")

    except requests.RequestException as error:
        print(f"API request failed: {error}")

    except KeyError as error:
        print(f"Unexpected API response: missing field {error}")


if __name__ == "__main__":
    main()