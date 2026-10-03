# Lab 13 - Sigma Detection Engineering

## Objective

Create a Sigma detection rule for suspicious PowerShell encoded-command activity, validate the rule, convert it to Splunk SPL, and test the detection against PowerShell Event ID 4104 telemetry.

## Environment

- Windows 11 VM
- PowerShell
- Sigma CLI
- Splunk Enterprise
- Splunk Universal Forwarder
- PowerShell Script Block Logging

## Tasks Performed

- Created a Sigma YAML detection rule
- Installed Sigma CLI
- Installed the Splunk backend plugin
- Selected the `splunk_windows` processing pipeline
- Converted the Sigma rule to Splunk SPL
- Forwarded PowerShell Operational logs to Splunk
- Verified Event ID 4104 ingestion
- Tested the detection against controlled PowerShell activity

## Detection Logic

The Sigma rule searched for PowerShell script block content containing:

- `FromBase64String`
- `EncodedCommand`
- `ToBase64String`

## MITRE ATT&CK

**T1059.001 - Command and Scripting Interpreter: PowerShell**

## Splunk Conversion

The Sigma rule was successfully converted into Splunk detection logic using the Splunk backend.

## Test Result

The detection successfully matched controlled PowerShell Event ID 4104 telemetry in Splunk.

## Detection Assessment

- Rule status: Successfully validated
- Backend: Splunk
- Pipeline: `splunk_windows`
- Result: Detection logic successfully tested
- Expected false positives:
  - Administrative scripts
  - Security tools
  - Authorized lab activity

## Skills Demonstrated

- Sigma rule creation
- Detection engineering
- YAML
- Sigma CLI
- Splunk SPL
- PowerShell telemetry analysis
- Event ID 4104 investigation
- MITRE ATT&CK mapping
- Detection testing and validation

## Evidence

Supporting screenshots and the Lab 13 PDF report are included in this folder.

## Safety Note

All PowerShell activity used for validation was harmless and generated inside an authorized lab environment.
