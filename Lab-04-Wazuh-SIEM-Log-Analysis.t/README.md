
# Lab 04 - Wazuh SIEM Log Analysis

## Objective

Deploy a Wazuh SIEM environment, connect a Windows 11 endpoint, collect Windows security telemetry, and investigate authentication activity through the Wazuh dashboard.

## Environment

- Ubuntu Server
- Wazuh all-in-one deployment
- Windows 11 VM
- Wazuh Windows Agent
- VMware Workstation

## Architecture

Windows 11 endpoint  
→ Wazuh Agent  
→ Wazuh Manager  
→ Wazuh Indexer  
→ Wazuh Dashboard

## Tasks Performed

- Installed the Wazuh Manager, Indexer, and Dashboard
- Configured an Ubuntu Server as the Wazuh SIEM server
- Installed the Wazuh Agent on Windows 11
- Enrolled and registered the Windows endpoint
- Verified agent connectivity
- Collected Windows Security Event Logs
- Investigated authentication-related events
- Reviewed failed and successful logon activity
- Troubleshot agent registration and connectivity issues
- Verified events in the Wazuh Threat Hunting interface

## Key Findings

The Windows endpoint successfully transmitted security telemetry to the Wazuh SIEM.

Authentication events could be searched and investigated through the Wazuh dashboard, demonstrating centralized security log collection and analysis.

The lab also provided practical experience troubleshooting agent connectivity, enrollment, and event ingestion issues.

## Skills Demonstrated

- SIEM deployment
- Wazuh administration
- Windows endpoint monitoring
- Agent enrollment and management
- Windows Event Log analysis
- Security log ingestion
- Threat hunting
- SIEM troubleshooting
- Linux administration

## Evidence

Supporting screenshots and the full Wazuh SIEM lab report are included in this folder.

## Safety Note

All monitoring and testing were performed on authorized virtual machines in a controlled lab environment.
