## **Incident Handler’s Journal**

### **Purpose**

This journal documents incident response activities, investigations, and key cybersecurity concepts encountered during training. It serves as a record of applied learning and analytical thinking related to security incidents and defensive tools.

---

### **Date: September 09, 2025**

**Entry \#:** 1

#### **Description**

A phishing email containing a malicious attachment was sent to a small U.S.-based healthcare clinic. When an employee downloaded the attachment, ransomware executed on the system and encrypted critical files. A ransom note was left demanding payment in exchange for a decryption key.

#### **Tool(s) Used**

None

#### **The 5 W’s**

* **Who:** An organized group of unethical hackers

* **What:** A ransomware attack delivered via a phishing email

* **When:** Tuesday at approximately 9:00 a.m.

* **Where:** A healthcare clinic

* **Why:** The attackers successfully exploited a phishing email to gain initial access to the system. Their motivation was financial gain, as evidenced by the ransom demand for the decryption key.

#### **Additional Notes**

To prevent future incidents of this type, the organization could implement:

* Security awareness training focused on phishing recognition

* Email filtering and attachment sandboxing

* Regular system backups stored offline

* Endpoint protection and anti-malware solutions

* Least-privilege access controls

---

### **Date: September 19, 2025**

**Entry \#:** 2

#### **Description**

Network packets were captured and analyzed as part of an investigation. A packet sniffer was used to inspect traffic and identify relevant packet details related to the incident.

#### **Tool(s) Used**

Wireshark

#### **Findings**

I applied an IP address filter in Wireshark using:

`ip.addr == 142.250.1.139`

This filter narrowed the results to packets using the TCP, ICMP, and HTTP protocols. By inspecting the packet details pane, I identified that the packet of interest (UTC) arrived on November 23, 2022 at approximately 12:38:34.

#### **Additional Notes**

Filtering traffic by IP address significantly reduced noise and allowed for more efficient packet analysis. This investigation reinforced the importance of understanding network protocols and timestamps when analyzing potential security incidents.

---

### 

### **Date: October 03, 2025**

**Entry \#:** 3

#### **Description**

A security alert was generated indicating multiple failed login attempts followed by a successful login from an unfamiliar IP address. This activity suggested a potential brute-force or credential-stuffing attack.

#### **Tool(s) Used**

SIEM (log analysis), authentication logs

#### **The 5 W’s**

* **Who:** An unknown external actor

* **What:** Suspicious authentication activity indicating possible account compromise

* **When:** Early morning hours outside normal business operations

* **Where:** User authentication system

* **Why:** Weak or reused credentials may have been exploited, allowing an attacker to gain access after repeated failed attempts.

#### **Additional Notes**

Recommended mitigation steps include:

* Enforcing multi-factor authentication (MFA)

* Monitoring failed login thresholds and alerting

* Implementing strong password policies

* Reviewing account access logs for lateral movement

