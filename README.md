# Cybersecurity SOC Portfolio

Hi, I'm **Dulanjana Bandara**, a Computer Science graduate with practical hands-on experience in SOC analysis, SIEM monitoring, Windows event investigation, network traffic analysis, phishing investigation, malware triage, incident response, and detection engineering.

This repository documents my cybersecurity lab work and portfolio projects developed while preparing for entry-level roles such as:

- SOC Analyst
- Junior SOC Analyst
- Cybersecurity Analyst
- Security Operations Analyst
- Associate Cybersecurity Analyst

---

## About Me

I completed my degree through:

**INFORMATICS INSTITUTE OF TECHNOLOGY**  
**In Collaboration with**  
**UNIVERSITY OF WESTMINSTER, UK**

### Degree

**BSc (Hons) Computer Science — Upper Second Class Honours**

I also have approximately **one year of industry experience as a Software Engineer Intern at Sarasa Soft Solutions**, where I gained experience working in a professional software development environment.

My current focus is cybersecurity, particularly:

- Security Operations
- SOC Monitoring
- SIEM Investigation
- Incident Triage
- Detection Engineering
- Endpoint Security
- Network Traffic Analysis

---

# Core Cybersecurity Skills

## SIEM and Security Monitoring

- Splunk Enterprise
- Splunk Universal Forwarder
- Splunk SPL
- Wazuh SIEM
- Windows Security Event Logs
- Microsoft Defender telemetry
- Alert triage
- Detection logic
- Security dashboards

## Windows and Endpoint Security

- Windows Event Viewer
- Event ID 4624
- Event ID 4625
- Event ID 4104
- Defender Event ID 1116
- Defender Event ID 1117
- PowerShell Script Block Logging
- Microsoft Defender
- Endpoint telemetry analysis

## Network Security

- Wireshark
- DNS analysis
- TCP three-way handshake
- TLS analysis
- Network ports and protocols
- Packet inspection
- Network troubleshooting

## Threat Investigation

- Phishing analysis
- Email header analysis
- SPF / DKIM / DMARC
- IOC extraction
- Malware triage
- Malware sandbox analysis
- Incident timelines
- MITRE ATT&CK mapping
- SOC alert triage
- Blast-radius analysis

## Detection Engineering

- Sigma rule creation
- Sigma CLI
- Splunk detection conversion
- SPL detection logic
- PowerShell detection
- Alert testing and validation

## Platforms and Tools

- Windows 11
- Ubuntu Server
- VMware Workstation
- PowerShell
- Linux CLI
- Splunk
- Wazuh
- Microsoft Defender
- Wireshark
- Sigma

---

# Featured Projects

## Splunk SIEM Investigation

Built a Splunk Enterprise lab and connected a Windows 11 endpoint using the Splunk Universal Forwarder.

### Work Completed

- Installed Splunk Enterprise on Ubuntu Server
- Configured TCP receiving on port 9997
- Installed and configured Splunk Universal Forwarder
- Forwarded Windows Security logs
- Investigated Event IDs 4624 and 4625
- Created SPL queries
- Built failed-logon detection logic
- Created a scheduled Splunk alert
- Successfully triggered the alert
- Built a Windows Authentication Monitoring dashboard

[View Project](./Lab-08-Splunk-SIEM-Investigation/)

---

## Full SOC Incident Investigation

Performed a controlled SOC investigation using Windows telemetry, Wazuh, PowerShell logging, and Microsoft Defender.

### Evidence Investigated

- Event ID 4625 - Failed authentication
- Event ID 4624 - Successful authentication
- Event ID 4104 - PowerShell Script Block Logging
- Event ID 1116 - Defender detection
- Event ID 1117 - Defender remediation

### Key Work

- Correlated multiple security events
- Built an incident timeline
- Investigated authentication activity
- Reviewed PowerShell telemetry
- Verified endpoint detection
- Confirmed Defender quarantine
- Distinguished controlled testing from evidence of real compromise

[View Project](./Lab-07-Full-SOC-Incident-Investigation/)

---

## Sigma Detection Engineering

Created and tested a Sigma detection rule for suspicious PowerShell encoded-command activity.

### Work Completed

- Created a Sigma YAML rule
- Installed Sigma CLI
- Installed the Splunk backend
- Used the `splunk_windows` pipeline
- Converted the Sigma rule into Splunk SPL
- Forwarded PowerShell Operational logs into Splunk
- Verified Event ID 4104 telemetry
- Tested and validated detection logic

### MITRE ATT&CK

**T1059.001 - Command and Scripting Interpreter: PowerShell**

[View Project](./Lab-13-Sigma-Detection-Engineering/)

---

## Malware Sandbox Analysis

Analyzed a public Agent Tesla sandbox report without executing malware locally.

### Key Findings

- Browser credential theft
- Browser cookie access
- Outlook profile access
- External IP discovery
- Host discovery
- Registry Run-key persistence
- Suspicious FTP communication

### Detection and Analysis

- IOC extraction
- Registry persistence analysis
- Network activity analysis
- MITRE ATT&CK mapping
- SOC triage and response planning

[View Project](./Lab-12-Malware-Sandbox-Analysis/)

---

## Advanced Phishing Investigation

Performed a SOC-style phishing investigation using a simulated Microsoft 365 phishing email.

### Analysis Included

- Sender / Reply-To mismatch
- Lookalike domain detection
- SPF / DKIM / DMARC analysis
- Suspicious URL analysis
- IOC extraction
- Blast-radius assessment
- Severity classification
- SOC response recommendations

[View Project](./Lab-10-Advanced-Phishing-Investigation/)

---

## Wazuh SIEM Deployment and Log Analysis

Deployed a Wazuh all-in-one SIEM environment on Ubuntu Server and connected a Windows 11 endpoint.

### Work Completed

- Installed Wazuh Manager
- Installed Wazuh Indexer
- Installed Wazuh Dashboard
- Enrolled Windows agents
- Collected Windows Security telemetry
- Investigated authentication events
- Forwarded Microsoft Defender logs
- Used Threat Hunting
- Troubleshot agent connectivity
- Reviewed SIEM alerts

[View Project](./Lab-04-Wazuh-SIEM-Log-Analysis/)

---

# Completed Cybersecurity Labs

| Lab | Project | Main Skills |
|---|---|---|
| 01 | Windows Event Log Investigation | Event IDs 4624/4625, authentication analysis |
| 02 | Wireshark Traffic Analysis | DNS, TCP, TLS, packet analysis |
| 03 | Phishing Email Investigation | Email triage, IOC extraction, ATT&CK |
| 04 | Wazuh SIEM Log Analysis | SIEM deployment, log ingestion, agents |
| 05 | Malware Triage | Defender, EICAR, Wazuh correlation |
| 06 | MITRE ATT&CK Investigation | ATT&CK mapping, analyst interpretation |
| 07 | Full SOC Incident Investigation | Incident timeline, endpoint telemetry, triage |
| 08 | Splunk SIEM Investigation | SPL, Universal Forwarder, alerts, dashboards |
| 09 | Three-Alert SOC Triage | Severity, verdict, escalation decisions |
| 10 | Advanced Phishing Investigation | SPF, DKIM, DMARC, IOCs, blast radius |
| 11 | Encoded PowerShell Investigation | Base64 decoding, Event ID 4104 |
| 12 | Malware Sandbox Analysis | Malware behavior, persistence, network IOCs |
| 13 | Sigma Detection Engineering | Sigma, SPL conversion, detection testing |

---

# Lab Repository

## Lab 01
[Windows Event Log Investigation](./Lab-01-Windows-Event-Log-Investigation/)

## Lab 02
[Wireshark Traffic Analysis](./Lab-02-Wireshark-Traffic-Analysis/)

## Lab 03
[Phishing Email Investigation](./Lab-03-Phishing-Email-Investigation/)

## Lab 04
[Wazuh SIEM Log Analysis](./Lab-04-Wazuh-SIEM-Log-Analysis/)

## Lab 05
[Malware Triage](./Lab-05-Malware-Triage/)

## Lab 06
[MITRE ATT&CK Investigation](./Lab-06-MITRE-ATTACK-Investigation/)

## Lab 07
[Full SOC Incident Investigation](./Lab-07-Full-SOC-Incident-Investigation/)

## Lab 08
[Splunk SIEM Investigation](./Lab-08-Splunk-SIEM-Investigation/)

## Lab 09
[Three-Alert SOC Triage](./Lab-09-Three-Alert-SOC-Triage/)

## Lab 10
[Advanced Phishing Investigation](./Lab-10-Advanced-Phishing-Investigation/)

## Lab 11
[Encoded PowerShell Investigation](./Lab-11-Encoded-PowerShell-Investigation/)

## Lab 12
[Malware Sandbox Analysis](./Lab-12-Malware-Sandbox-Analysis/)

## Lab 13
[Sigma Detection Engineering](./Lab-13-Sigma-Detection-Engineering/)

---

# Professional Experience

## Software Engineer Intern
**Sarasa Soft Solutions**

Approximately one year of industry experience in a software engineering environment.

### Experience Gained

- Software development
- Debugging and troubleshooting
- Technical problem solving
- Working with production-style systems
- Team-based development workflows
- Application behavior analysis
- Professional software engineering practices

This background supports my cybersecurity work by giving me practical experience understanding applications, systems, and technical troubleshooting.

---

# Final Year Project

## Neonatal Jaundice Detection Using a Computer Vision System

Developed a computer vision system designed to support neonatal jaundice detection using medical image analysis.

### Technologies and Methods

- Python
- TensorFlow / Keras
- EfficientNetB4
- Transfer learning
- Image preprocessing
- Illumination correction
- ROI extraction
- Color normalization
- Stratified K-fold cross-validation
- Threshold optimization
- Web-based deployment

### Skills Developed

- Machine learning
- Computer vision
- Deep learning
- Data preprocessing
- Model evaluation
- Research methodology
- Technical documentation
- End-to-end project development

---

# Portfolio Evidence

Individual lab folders contain available evidence such as:

- Lab documentation
- PDF investigation reports
- Screenshots
- SPL queries
- Wireshark packet captures
- Detection logic
- IOC tables
- Analyst findings

Evidence varies between projects depending on the material retained during each exercise.

---

# Ethical and Safety Statement

All cybersecurity testing documented in this repository was performed in authorized and controlled lab environments.

No unauthorized systems were targeted.

Safe simulations, public sandbox reports, and test artifacts were used where appropriate.

No real malware was executed on local systems.

Sensitive information such as passwords, authentication keys, personal email addresses, and private credentials has been removed or redacted.

---

# Career Focus

I am currently preparing for entry-level cybersecurity roles including:

- SOC Analyst
- Junior SOC Analyst
- Cybersecurity Analyst
- Security Operations Analyst
- Associate Cybersecurity Analyst

My current focus includes SIEM investigation, incident triage, detection engineering, endpoint telemetry, network analysis, Splunk, Wazuh, Microsoft Defender, Sigma, and Microsoft Sentinel.
