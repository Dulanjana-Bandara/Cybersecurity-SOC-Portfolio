# Lab 11 - Encoded PowerShell Investigation

## Objective

Investigate a safe Base64-encoded PowerShell command, decode the command, review PowerShell Script Block Logging, and determine whether the activity is benign or malicious.

## Environment

- Windows 11 VM
- PowerShell
- Windows Event Viewer
- PowerShell Script Block Logging
- VMware Workstation

## Tasks Performed

- Created a harmless PowerShell command
- Encoded the command using Base64
- Executed it with PowerShell `-EncodedCommand`
- Decoded the Base64 content
- Verified Event ID 4104 in PowerShell Script Block Logging
- Reviewed the decoded command from an analyst perspective
- Mapped the behavior to MITRE ATT&CK T1059.001

## Key Finding

The encoded command decoded to:

`Write-Output "LAB11 Encoded PowerShell Test"`

Event ID 4104 captured the decoded script content.

## Triage Decision

- Severity: Low
- Verdict: Benign / authorized test activity
- Escalation: No

## MITRE ATT&CK

**T1059.001 - Command and Scripting Interpreter: PowerShell**

## Skills Demonstrated

- PowerShell investigation
- Base64 decoding
- Event ID 4104 analysis
- Script Block Logging
- MITRE ATT&CK mapping
- SOC triage

## Evidence

Supporting screenshots and the Lab 11 PDF report are included in this folder.

## Safety Note

Only harmless PowerShell activity was used. No malicious payload was executed.
