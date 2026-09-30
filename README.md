# Cybersecurity SOC Portfolio

Hi, I'm **Dulanjana Bandara**, a Computer Science graduate building practical experience for entry-level **SOC Analyst**, **Cybersecurity Analyst**, and **Security Operations** roles.

This repository documents my hands-on cybersecurity labs covering SIEM monitoring, Windows event analysis, network traffic analysis, phishing investigation, malware triage, MITRE ATT&CK mapping, incident investigation, detection engineering, and Splunk-based security monitoring.

---

## About Me

I completed my Computer Science degree through:

**INFORMATICS INSTITUTE OF TECHNOLOGY**  
**In Collaboration with**  
**UNIVERSITY OF WESTMINSTER**

I also have approximately **one year of industry experience as a Software Engineer Intern at Sarasa Soft Solutions**, where I gained experience working in a professional software development environment.

My current focus is transitioning into cybersecurity, particularly roles involving:

- SOC operations
- Security monitoring
- SIEM investigation
- Incident triage
- Threat detection
- Endpoint monitoring
- Network traffic analysis

---

## Education

**BSc (Hons) Computer Science**

**Informatics Institute of Technology**  
In Collaboration with  
**University of Westminster**

---

## Professional Experience

### Software Engineer Intern  
**Sarasa Soft Solutions**

Approximately one year of industry experience in a software engineering environment.

### Experience gained

- Software development
- Debugging and troubleshooting
- Working with production-style systems
- Technical problem solving
- Team-based development workflows
- Understanding application behavior from a developer perspective

This software development background supports my cybersecurity learning by giving me a stronger understanding of applications, systems, code, and technical troubleshooting.

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

## Network Security

- Wireshark
- DNS analysis
- TCP three-way handshake
- TLS traffic analysis
- Network ports and protocols
- Basic traffic investigation

## Endpoint and Windows Security

- Windows Event Viewer
- Event ID 4624
- Event ID 4625
- Event ID 4104
- Defender Event ID 1116
- Defender Event ID 1117
- PowerShell Script Block Logging
- Endpoint detection analysis

## Threat Investigation

- Phishing email analysis
- IOC identification
- Malware triage
- Incident timelines
- MITRE ATT&CK mapping
- SOC-style investigation
- Evidence-based analyst decision-making

## Platforms and Tools

- Windows 11
- Ubuntu Server
- VMware Workstation
- PowerShell
- Linux command line
- Splunk
- Wazuh
- Microsoft Defender
- Wireshark

---

# Featured Projects

## Splunk SIEM Investigation

Built a Splunk Enterprise lab environment and connected a Windows 11 endpoint using the Splunk Universal Forwarder.

### Work completed

- Installed Splunk Enterprise on Ubuntu Server
- Configured TCP receiving on port 9997
- Installed and configured Splunk Universal Forwarder
- Forwarded Windows Security Event Logs
- Investigated Event IDs 4624 and 4625
- Used SPL for authentication analysis
- Created field extraction using regular expressions
- Built a failed-logon detection search
- Created a scheduled Splunk alert
- Successfully triggered the alert
- Built a Windows Authentication Monitoring dashboard

[View Project](./Lab-08-Splunk-SIEM-Investigation/)

---

## Full SOC Incident Investigation

Performed a controlled SOC investigation using Windows telemetry, Wazuh, PowerShell logging, and Microsoft Defender.

### Evidence investigated

- Event ID 4625 - Failed authentication
- Event ID 4624 - Successful authentication
- Event ID 4104 - PowerShell Script Block Logging
- Event ID 1116 - Microsoft Defender detection
- Event ID 1117 - Defender remediation

### Key work

- Correlated multiple security events
- Built an incident timeline
- Investigated authentication activity
- Reviewed PowerShell telemetry
- Verified endpoint detection
- Confirmed Defender quarantine
- Differentiated controlled lab activity from evidence of real compromise

[View Project](./Lab-07-Full-SOC-Incident-Investigation/)

---

## Wazuh SIEM Deployment and Log Analysis

Deployed a Wazuh all-in-one SIEM environment on Ubuntu Server and connected a Windows 11 endpoint.

### Work completed

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

## Malware Triage with Microsoft Defender and Wazuh

Performed safe endpoint detection testing using the EICAR antivirus test artifact.

### Work completed

- Generated controlled EICAR test activity
- Observed Microsoft Defender detection
- Investigated Defender Event ID 1116
- Verified quarantine using Event ID 1117
- Correlated Defender telemetry with Wazuh
- Reviewed Wazuh severity and alert details
- Recorded the SHA-256 hash
- Documented SOC-style triage findings

No real malware was executed during this lab.

[View Project](./Lab-05-Malware-Triage/)

---

## Wireshark Traffic Analysis

Captured and analyzed network traffic using Wireshark.

### Protocols investigated

- DNS
- TCP
- TLS

### Work completed

- Identified DNS queries and responses
- Analyzed TCP SYN, SYN-ACK, and ACK packets
- Reviewed TLS ClientHello and ServerHello traffic
- Identified SNI values where visible
- Examined source and destination ports
- Practiced basic SOC network analysis

[View Project](./Lab-02-Wireshark-Traffic-Analysis/)

---

## Phishing Email Investigation

Analyzed a simulated phishing email and documented indicators associated with phishing activity.

### Investigation included

- Sender analysis
- Reply-To mismatch
- Suspicious links
- Urgency indicators
- Email authentication indicators
- IOC extraction
- MITRE ATT&CK mapping

[View Project](./Lab-03-Phishing-Email-Investigation/)

---

# Completed Labs

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

---

# Final Year Project

## Neonatal Jaundice Detection Using a Computer Vision System

For my final year project, I developed a computer vision system designed to support neonatal jaundice detection using medical image analysis.

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

### Project Work

The project involved:

- Preparing and preprocessing neonatal image data
- Applying transfer learning
- Training and evaluating a deep learning model
- Comparing validation and test performance
- Optimizing classification thresholds
- Developing a web-based prototype
- Evaluating model performance for practical use

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

# Upcoming Portfolio Projects

This portfolio will continue to be updated with:

- Three-Alert SOC Triage
- Advanced Phishing Investigation
- Encoded PowerShell Investigation
- Malware Sandbox Analysis
- Sigma Detection Engineering
- Microsoft Sentinel Investigation

---

# Lab Environment

Most labs were performed using:

- VMware Workstation
- Windows 11 virtual machines
- Ubuntu Server
- Splunk Enterprise
- Splunk Universal Forwarder
- Wazuh
- Microsoft Defender
- Wireshark
- PowerShell

---

# Portfolio Evidence

Where available, individual lab folders contain:

- Lab documentation
- PDF investigation reports
- Screenshots
- SPL queries
- Wireshark packet captures
- Detection logic
- Investigation findings

Evidence differs between labs depending on what was retained during the exercise.

---

# Ethical and Safety Statement

All security testing documented in this repository was performed in authorized and controlled lab environments.

No unauthorized systems were targeted.

Safe simulations and test artifacts were used where appropriate.

No real malware was executed.

Sensitive information such as passwords, authentication keys, personal email addresses, and private credentials has been removed or redacted.

---

# Career Focus

I am currently developing practical skills for entry-level roles such as:

- SOC Analyst
- Junior SOC Analyst
- Cybersecurity Analyst
- Security Operations Analyst
- Associate Cybersecurity Analyst

My current learning focus includes SIEM investigation, detection engineering, endpoint telemetry, network analysis, incident response, Splunk, Wazuh, and Microsoft Sentinel.
