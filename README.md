# Cybersecurity SOC Portfolio

Hi, I'm Dulanjana Bandara, a Computer Science graduate building practical experience for entry-level SOC Analyst and Cybersecurity Analyst roles.

This repository documents my hands-on cybersecurity labs covering SIEM monitoring, Windows event analysis, network traffic analysis, phishing investigation, malware triage, MITRE ATT&CK mapping, incident investigation, and detection engineering.

## Core Skills

- SIEM: Splunk Enterprise, Wazuh
- Windows Security Event Analysis
- Splunk SPL
- Network Traffic Analysis with Wireshark
- Microsoft Defender
- PowerShell Logging
- MITRE ATT&CK
- Phishing Analysis
- Incident Triage and Investigation
- Linux Administration
- TCP/IP, DNS, TLS and HTTP/S fundamentals

---

# Featured Projects

## Splunk SIEM Investigation

Built a Splunk Enterprise lab environment and connected a Windows 11 endpoint using the Splunk Universal Forwarder.

### Work completed
- Installed Splunk Enterprise on Ubuntu Server
- Configured TCP receiving on port 9997
- Forwarded Windows Security logs
- Investigated Event IDs 4624 and 4625
- Created SPL queries for authentication monitoring
- Built a failed-logon detection
- Created and successfully triggered a scheduled Splunk alert
- Built a Windows Authentication Monitoring dashboard

[View project](./Lab-08-Splunk-SIEM-Investigation/)

---

## Full SOC Incident Investigation

Performed a controlled SOC investigation using Windows telemetry, Wazuh and Microsoft Defender.

### Evidence investigated
- Event ID 4625 — failed authentication
- Event ID 4624 — successful authentication
- Event ID 4104 — PowerShell Script Block Logging
- Event ID 1116 — Microsoft Defender detection
- Event ID 1117 — successful Defender quarantine

Created an evidence-based incident timeline and differentiated controlled test activity from evidence of a real compromise.

[View project](./Lab-07-Full-SOC-Incident-Investigation/)

---

## Wazuh SIEM Deployment and Log Analysis

Deployed a Wazuh all-in-one SIEM server on Ubuntu Server and connected a Windows 11 endpoint.

### Work completed
- Wazuh Manager, Indexer and Dashboard deployment
- Windows agent enrollment
- Windows Security Event collection
- Authentication monitoring
- Microsoft Defender telemetry ingestion
- SIEM troubleshooting and agent management

[View project](./Lab-04-Wazuh-SIEM-Log-Analysis/)

---

## Malware Triage with Microsoft Defender and Wazuh

Used the industry-standard EICAR antivirus test file to safely test endpoint detection and SIEM monitoring.

### Work completed
- Microsoft Defender detection
- Windows Defender Event ID 1116 investigation
- Wazuh correlation
- File hash analysis
- Successful quarantine verification
- SOC-style malware triage report

No real malware was executed during this lab.

[View project](./Lab-05-Malware-Triage/)

---

# Completed Labs

| Lab | Project | Main Skills |
|---|---|---|
| 01 | Windows Event Log Investigation | Event IDs 4624/4625, authentication analysis |
| 02 | Wireshark Traffic Analysis | DNS, TCP handshake, TLS |
| 03 | Phishing Email Investigation | Sender analysis, indicators, phishing triage |
| 04 | Wazuh SIEM Log Analysis | SIEM deployment, log ingestion, agents |
| 05 | Malware Triage | Defender, EICAR, Wazuh correlation |
| 06 | MITRE ATT&CK Investigation | ATT&CK mapping and analyst interpretation |
| 07 | Full SOC Incident Investigation | Timeline analysis, endpoint telemetry, incident triage |
| 08 | Splunk SIEM Investigation | SPL, Universal Forwarder, alerts, dashboards |

---

# Lab Repository

### Lab 01
[Windows Event Log Investigation](./Lab-01-Windows-Event-Log-Investigation/)

### Lab 02
[Wireshark Traffic Analysis](./Lab-02-Wireshark-Traffic-Analysis/)

### Lab 03
[Phishing Email Investigation](./Lab-03-Phishing-Email-Investigation/)

### Lab 04
[Wazuh SIEM Log Analysis](./Lab-04-Wazuh-SIEM-Log-Analysis/)

### Lab 05
[Malware Triage](./Lab-05-Malware-Triage/)

### Lab 06
[MITRE ATT&CK Investigation](./Lab-06-MITRE-ATTACK-Investigation/)

### Lab 07
[Full SOC Incident Investigation](./Lab-07-Full-SOC-Incident-Investigation/)

### Lab 08
[Splunk SIEM Investigation](./Lab-08-Splunk-SIEM-Investigation/)

---

# Upcoming Portfolio Projects

The portfolio will continue to be updated with:

- Three-Alert SOC Triage
- Advanced Phishing Investigation
- Encoded PowerShell Investigation
- Malware Sandbox Analysis
- Sigma Detection Engineering

---

# Environment

Most labs were performed using:

- VMware Workstation
- Windows 11
- Ubuntu Server
- Splunk Enterprise
- Splunk Universal Forwarder
- Wazuh
- Microsoft Defender
- Wireshark
- PowerShell

---

# Portfolio Note

All security testing in this repository was performed in controlled lab environments.

Safe simulation tools and test artifacts were used where appropriate. No real malware or unauthorized systems were used.

Sensitive information such as passwords, authentication keys, personal email addresses and private credentials has been excluded or redacted.
