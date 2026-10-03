# Lab 09 - Three-Alert SOC Triage

## Objective

Triage three separate security alerts as independent SOC tickets and determine severity, verdict, escalation requirements, and analyst reasoning.

## Environment

- Windows 11 VM
- Wazuh SIEM
- Microsoft Defender
- PowerShell
- VMware Workstation

## Alerts Triaged

### Alert 1 - Windows Event ID 4625

**Scenario:** Multiple failed local logon attempts.

**Observed evidence:**
- Event ID 4625
- Logon Type 2
- Source address `127.0.0.1`
- Wazuh authentication-failure alert

**Triage decision:**
- Severity: Low
- Verdict: Benign / expected lab activity
- Escalation: No

The failed logons were generated intentionally in the lab and did not show evidence of remote brute force or account compromise.

---

### Alert 2 - PowerShell Event ID 4104

**Scenario:** PowerShell security-policy query.

**Observed activity:**

The command exported the local security policy, searched for the `ResetLockoutCount` value, and removed the temporary file.

Observed result:

`ResetLockoutCount = 10`

**Triage decision:**
- Severity: Low
- Verdict: Benign / administrative activity
- Escalation: No

PowerShell is a dual-use tool, so the command content and surrounding context were reviewed before reaching the verdict.

---

### Alert 3 - Microsoft Defender Event ID 1116

**Scenario:** EICAR antivirus test artifact detected by Microsoft Defender.

**Observed evidence:**
- Defender detected `Virus:DOS/EICAR_Test_File`
- Event ID 1116 recorded the detection
- Event ID 1117 confirmed successful remediation / quarantine

**Triage decision:**
- Severity: Medium
- Verdict: True positive detection in a benign test context
- Escalation: No

The detection was valid, but the file was the harmless industry-standard EICAR antivirus test artifact used intentionally for security testing.

---

## Triage Summary

| Alert | Evidence | Severity | Verdict | Escalation |
|---|---|---|---|---|
| 1 | Event ID 4625 | Low | Benign / expected lab activity | No |
| 2 | Event ID 4104 | Low | Benign / administrative activity | No |
| 3 | Event ID 1116 / 1117 | Medium | True positive, benign test context | No |

## Key Lessons

- Alert severity depends on context
- A detection does not automatically mean an incident
- PowerShell activity should be evaluated using command content and surrounding evidence
- Automated SIEM mappings should not replace analyst judgment
- True-positive detections can still occur during authorized testing
- Separate alerts should not be presented as one attack chain without supporting evidence

## Skills Demonstrated

- SOC alert triage
- Severity classification
- Analyst verdicts
- Escalation decisions
- Windows Event Log analysis
- PowerShell telemetry review
- Microsoft Defender investigation
- Wazuh SIEM analysis
- Evidence-based incident reasoning

## Evidence

The full Lab 09 report is included in this folder.

## Safety Note

All alerts were generated through controlled and authorized lab activity.
