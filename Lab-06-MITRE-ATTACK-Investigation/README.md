# Lab 06 - MITRE ATT&CK Investigation

## Objective

Map selected security events from previous labs to relevant MITRE ATT&CK techniques and distinguish between observed evidence, automated tool mappings, and analyst interpretation.

## Environment

- Windows 11 VM
- Wazuh SIEM
- Microsoft Defender
- PowerShell
- MITRE ATT&CK framework
- VMware Workstation

## Scenarios Reviewed

This lab reviewed several controlled events from earlier exercises, including:

- Simulated phishing activity
- PowerShell execution
- Windows authentication failures
- Microsoft Defender EICAR detection

## Tasks Performed

- Reviewed security events from previous SOC labs
- Identified relevant ATT&CK tactics and techniques
- Compared automated Wazuh ATT&CK mappings with observed evidence
- Distinguished confirmed activity from assumptions
- Avoided treating unrelated events as a single confirmed attack chain
- Documented analyst reasoning and limitations

## ATT&CK Mapping Examples

### Phishing

The simulated phishing scenario was mapped to:

- **T1566.002 - Phishing: Spearphishing Link**
- Tactic: Initial Access

This mapping was based on the simulated email containing a suspicious link.

### PowerShell

Controlled PowerShell activity was mapped to:

- **T1059.001 - Command and Scripting Interpreter: PowerShell**
- Tactic: Execution

The observed PowerShell commands were benign lab actions and did not represent malicious execution.

### Wazuh Automated Mapping

Some Wazuh rules automatically included ATT&CK technique tags.

These automated mappings were reviewed critically rather than accepted as proof of attacker behavior.

## Key Findings

MITRE ATT&CK is useful for describing observed behaviors, but technique mapping must be based on evidence.

A SIEM rule or automated ATT&CK tag does not automatically prove malicious intent or a complete intrusion chain.

Separate controlled lab events should not be presented as causally linked unless the evidence supports that conclusion.

## Skills Demonstrated

- MITRE ATT&CK mapping
- Security event interpretation
- SOC analyst reasoning
- Evidence-based investigation
- SIEM rule review
- Distinguishing detection from attribution
- Incident documentation

## Analyst Assessment

The reviewed activity consisted of controlled lab simulations and defensive test events.

The exercise focused on correctly mapping observable behavior while avoiding unsupported conclusions about compromise, attacker intent, or attack-chain progression.

## Evidence

Supporting screenshots and the full MITRE ATT&CK investigation report are included in this folder.

## Safety Note

All activity was performed in an authorized virtual lab environment.

No real phishing campaign, malicious PowerShell payload, or unauthorized attack activity was used.
