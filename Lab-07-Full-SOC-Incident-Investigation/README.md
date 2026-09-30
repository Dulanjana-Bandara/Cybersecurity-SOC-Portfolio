# Lab 07 - Full SOC Incident Investigation

## Objective

Perform a full SOC-style investigation using Windows authentication events, PowerShell telemetry, Microsoft Defender detections, and Wazuh SIEM evidence.

## Environment

- Windows 11 VM
- Ubuntu Server
- Wazuh SIEM
- Microsoft Defender Antivirus
- PowerShell
- VMware Workstation

## Incident ID

**INC-007**

## Evidence Investigated

### Windows Authentication

- **Event ID 4625** - Failed logon
- **Event ID 4624** - Successful logon

The failed logon activity was generated intentionally in the lab and was followed by a successful local workstation unlock.

### PowerShell Activity

- **Event ID 4104** - PowerShell Script Block Logging

PowerShell logging was enabled and forwarded to Wazuh.

The investigation confirmed that PowerShell telemetry was successfully collected by the SIEM.

### Microsoft Defender Detection

- **Event ID 1116** - Malware or potentially unwanted software detected
- **Event ID 1117** - Defender remediation action

A safe EICAR antivirus test file was used.

Microsoft Defender successfully detected and quarantined the file.

## Wazuh Evidence

The Wazuh SIEM successfully collected and correlated:

- Windows authentication telemetry
- PowerShell Script Block Logging
- Microsoft Defender Operational events

The Defender detection generated a high-severity Wazuh alert.

## Incident Timeline

The investigation established a timeline containing:

1. Controlled failed authentication attempts
2. Successful workstation unlock
3. PowerShell activity
4. EICAR antivirus detection
5. Successful Defender quarantine

These events were generated as separate controlled lab activities and were not treated as evidence of a single real-world attack chain.

## Key Findings

- Windows authentication telemetry was successfully collected
- PowerShell Script Block Logging was successfully ingested
- Microsoft Defender detected the EICAR test artifact
- Defender successfully quarantined the artifact
- Wazuh correlated endpoint telemetry and generated alerts
- No evidence supported a real compromise, lateral movement, or malware infection

## Analyst Assessment

The final case classification was:

**Controlled security investigation / authorized test activity**

The exercise demonstrated how a SOC analyst can correlate endpoint and SIEM evidence while avoiding unsupported assumptions about attacker intent or compromise.

## Skills Demonstrated

- Incident investigation
- Timeline analysis
- Windows Event Log analysis
- PowerShell telemetry investigation
- Microsoft Defender investigation
- Wazuh SIEM correlation
- Alert triage
- Evidence-based analyst decision-making
- Incident reporting

## Evidence

Supporting screenshots and the full INC-007 investigation report are included in this folder.

## Safety Note

All activity was performed in an isolated and authorized lab environment.

The malware-related portion used only the harmless EICAR antivirus test artifact. No real malware was executed.
