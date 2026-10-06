# Lab 15 - Python Threat Intelligence API Automation

## Overview

Built a Python-based threat intelligence automation tool that validates IP addresses, queries the AbuseIPDB REST API, parses threat intelligence data, assigns a risk level, recommends an analyst action, and saves results in JSON and CSV formats.

## Tools Used

- Python
- AbuseIPDB REST API
- requests
- ipaddress
- JSON
- CSV
- Environment variables

## Workflow

```text
User IP Input
      |
      v
Input Validation
      |
      v
AbuseIPDB API
      |
      v
JSON Parsing
      |
      v
Risk Classification
      |
      v
Recommended Action
      |
      +--> JSON Report
      |
      +--> CSV Log
