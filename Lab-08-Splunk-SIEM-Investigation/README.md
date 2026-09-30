# Lab 08 - Splunk SIEM Investigation

## Objective

Deploy Splunk Enterprise, connect a Windows 11 endpoint using the Splunk Universal Forwarder, ingest Windows Security logs, investigate authentication events, create SPL detection logic, and build an alerting dashboard.

## Environment

- Ubuntu Server 24.04 LTS
- Splunk Enterprise
- Splunk Universal Forwarder
- Windows 11 VM
- VMware Workstation

## Architecture

Windows 11 Security Logs  
→ Splunk Universal Forwarder  
→ Splunk Enterprise Indexer  
→ Search & Reporting  
→ Detection Alert  
→ Dashboard

## Tasks Performed

- Installed Splunk Enterprise on Ubuntu Server
- Configured Splunk to receive forwarded data on TCP port 9997
- Installed Splunk Universal Forwarder on Windows 11
- Configured forwarding to the Splunk server
- Enabled Windows Security Event Log collection
- Verified successful log ingestion
- Investigated Event IDs 4624 and 4625
- Used SPL and regular expressions to extract Event IDs and authentication fields
- Created a failed-logon detection search
- Configured a scheduled alert using a cron schedule
- Successfully triggered the alert using controlled failed login attempts
- Built a Windows Authentication Monitoring dashboard

## Authentication Events

### Event ID 4624

Represents successful Windows authentication activity.

### Event ID 4625

Represents failed Windows authentication activity.

Controlled failed login attempts were generated to validate the detection workflow.

## SPL Investigation

Windows authentication events were identified using SPL searches against:

`index=main`

and the Windows Security XML sourcetype.

Regular expression extraction was used to identify Event IDs from raw XML data.

## Failed Logon Detection

A detection search was created to identify multiple failed logons within the search window.

The detection summarized:

- Host
- Source IP
- Logon Type
- Failed login count
- First observed time
- Last observed time

The controlled test produced multiple Event ID 4625 events from:

`127.0.0.1`

with:

`LogonType = 2`

indicating local interactive authentication activity.

## Splunk Alert

A scheduled alert named:

**Multiple Failed Windows Logons**

was created.

Configuration included:

- Scheduled execution
- Cron schedule
- Trigger when number of results is greater than 0
- Trigger once
- Throttling to reduce duplicate alerts
- Add to Triggered Alerts

The alert was successfully triggered during a controlled failed-login test.

## Dashboard

A dashboard named:

**Windows Authentication Monitoring**

was created.

### Dashboard Panels

1. **Successful vs Failed Logons**
   - Visual comparison of Event IDs 4624 and 4625

2. **Failed Logon Summary**
   - Host
   - Source IP
   - Logon Type
   - Event count

## Key Findings

- Windows Security logs were successfully forwarded into Splunk
- Authentication events were searchable through SPL
- Failed login activity could be grouped and summarized
- A custom scheduled detection successfully triggered
- Dashboard visualizations provided a simple authentication monitoring view

## Analyst Assessment

The observed failed logon events were generated intentionally in a controlled lab environment.

The activity represented local interactive authentication failures and did not indicate a confirmed remote brute-force attack.

## Skills Demonstrated

- Splunk Enterprise deployment
- Splunk Universal Forwarder
- Windows log ingestion
- SPL
- Field extraction
- Authentication monitoring
- Detection engineering
- Scheduled alert creation
- SIEM dashboard development
- SOC investigation workflow
- Linux administration

## Evidence

Supporting screenshots and the full Splunk SIEM investigation report are included in this folder.

## Safety Note

All testing was performed against authorized virtual machines in a controlled lab environment.

No unauthorized systems or real attack activity were used.
