# Lab 10 - Advanced Phishing Investigation

## Objective

Perform a SOC-style phishing investigation using a safe simulated email sample and evaluate sender identity, authentication results, suspicious infrastructure, indicators of compromise, blast radius, severity, and response actions.

## Scenario

A simulated Microsoft 365 security email claimed that unusual account activity had been detected and threatened account suspension unless the user verified the account within 24 hours.

## Email Indicators

### Sender

`security-alert@micros0ft-support.com`

The sender domain used the digit `0` instead of the letter `o`, making it a lookalike / typosquatted Microsoft-style domain.

### Reply-To

`support-team@account-verification-help.com`

The Reply-To domain was different from the sender domain.

### Verification URL

`https://microsoft-security-check.example-login.com/verify`

The real registrable domain was:

`example-login.com`

and not a legitimate Microsoft domain.

## Email Authentication

The simulated message contained:

- SPF: Fail
- DKIM: None
- DMARC: Fail

These authentication results increased suspicion when combined with the other phishing indicators.

## Suspicious Indicators

The investigation identified:

- Sender / Reply-To mismatch
- Lookalike sender domain
- Urgent account-suspension language
- Non-Microsoft verification domain
- SPF failure
- Missing DKIM
- DMARC failure

## IOC Extraction

| IOC Type | Value | Assessment |
|---|---|---|
| Sender domain | `micros0ft-support.com` | Lookalike / typosquatted domain |
| Reply-To domain | `account-verification-help.com` | Different domain from sender |
| Verification domain | `example-login.com` | Non-Microsoft destination |
| Verification path | `/verify` | Credential-verification lure path |

## Blast-Radius Analysis

If this email were reported in a real organization, the next investigation steps would include:

- Determine whether other users received the same message
- Check whether any users clicked the link
- Determine whether credentials were submitted
- Search mailboxes for matching messages
- Remove malicious messages where possible
- Review affected accounts for suspicious sign-in activity

## Triage Decision

- Severity: High
- Verdict: Phishing / malicious
- Escalation: Yes

The combination of sender impersonation, failed authentication, urgent social-engineering language, and a suspicious verification destination strongly supported a phishing verdict.

## Recommended SOC Response

- Block the phishing sender and domains
- Block the malicious verification URL
- Search the mail environment for matching messages
- Remove malicious emails from user mailboxes
- Investigate users who clicked the link
- Reset credentials if credential submission is suspected
- Review MFA status
- Review sign-in logs for suspicious authentication activity
- Document the IOCs for future detection and threat hunting

## Skills Demonstrated

- Phishing investigation
- Email authentication analysis
- SPF / DKIM / DMARC interpretation
- Sender and Reply-To analysis
- Typosquatting identification
- IOC extraction
- Blast-radius assessment
- SOC escalation decisions
- Incident-response recommendations

## Evidence

The full Lab 10 investigation report is included in this folder.

## Safety Note

This lab used a simulated phishing email only.

No live phishing infrastructure, malicious attachment, or credential-harvesting page was accessed.
