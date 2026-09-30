# Lab 01 - Windows Event Log Investigation

## Objective

Investigate Windows authentication activity using Windows Security Event Logs and identify failed and successful logon events.

## Environment

- Windows 11 VM
- VMware Workstation
- Windows Event Viewer

## Key Event IDs

- **4624** - Successful logon
- **4625** - Failed logon

## Tasks Performed

- Generated controlled failed login attempts
- Reviewed Windows Security logs
- Filtered authentication events
- Investigated Event ID 4625
- Compared failed logons with successful Event ID 4624 activity
- Identified timestamps, logon types, and authentication details

## Findings

The investigation showed failed local authentication attempts followed by a successful login.

The observed activity was generated intentionally in a controlled lab environment and did not indicate a real compromise.

## Skills Demonstrated

- Windows Event Log analysis
- Authentication monitoring
- Event ID investigation
- SOC triage fundamentals
- Windows Security auditing

## Evidence

Supporting screenshots and the full lab report are included in this folder.

## Safety Note

All activity was performed in an isolated lab environment using controlled test actions.
