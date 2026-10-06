# Lab 14 - SOAR Alert Enrichment & Analyst Escalation

## Overview

Built a SOAR-style security automation workflow in Tines to receive a simulated Splunk alert, extract an IP indicator, enrich it using AbuseIPDB, classify the risk, and route the event automatically based on severity.

## Tools Used

- Tines Community Edition
- AbuseIPDB
- REST API
- Webhooks
- JSON
- Conditional workflow logic

## Workflow

```text
Simulate Splunk Alert
        |
        v
Receive Security Alert
        |
        v
Check IP with AbuseIPDB
        |
        v
Classify Risk and Build Summary
        |
        v
      High Risk?
       /     \
     Yes      No
      |        |
      v        v
Generate     Finalize
Analyst      Low/Medium
Escalation   Alert
