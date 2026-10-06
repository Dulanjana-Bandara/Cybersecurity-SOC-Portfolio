# Lab 16 - Microsoft Sentinel & Entra ID Cloud Security Monitoring

## Overview

Built a cloud security monitoring lab using Microsoft Sentinel, Log Analytics, and Microsoft Entra ID.

The lab connected Entra audit activity to Sentinel, generated a controlled identity-management event, and investigated the activity using Kusto Query Language (KQL).

## Tools Used

- Microsoft Azure
- Microsoft Sentinel
- Log Analytics
- Microsoft Entra ID
- AuditLogs
- Kusto Query Language (KQL)

## Workflow

```text
Microsoft Entra ID
        |
        v
Audit Logs
        |
        v
Log Analytics Workspace
        |
        v
Microsoft Sentinel
        |
        v
KQL Investigation
