# Introduction to Ethical Hacking

### Terminology 

* Hack Value : something is worth doing
* Vulnerability : weakness, design or implementation error
* Exploit : breach
* Payload : part of an exploit code
* Zero-Day attack : computer application vulnerabilities
* Daisy Chaining : Gaining access to one network and/or computer
* Doxing : Publishing personally identifiable information
* Bot : controlled remotely to execute or automate predefined tasks


### Elements of information security

* Confidentiality
* Integrity
* Availability
* Authenticity
* Non-Repudiation : Guarantee that the sender of a message cannot later deny having sent the message

Attacks = Motive (Goal) + Method + Vulnerability

##### Threats Categories
Network threats
 * Information gathering
 * Spoofing
 * ...
 
Host threats
 * Malware
 * Footprinting
 * ...
 
Application threats
 * SQL Injection
 * Buffer overflow
 * ...
 
### Hacker

##### Hacker type
* White hat
* Black hat
* Grey hat
* Script Kiddies
* Cyber terrorists
* Hacktivist
* ...

##### Phases

1. Reconnaissance
    * Passive (without directly interacting with the target)
    * Active (interacting with the target)
2. Scanning
3. Gaining access
4. Maintaining access
5. Cleaning tracks


### Information Security Controls

##### ISMP : Information Security Management Program
Defense-in-depth : several layer of protection

![Defense in Depth](http://3.bp.blogspot.com/-XECwfFF2KOk/URMlV5vwsaI/AAAAAAAAACo/NtaOQMhniJA/s1600/img_defense-in-depth.jpg)

##### Security Policies
* Access Control policy
* Remote Access policy
* Firewall Management policy
* Network Connection policy
* Password policy
* User account policy
* Information-Protection policy
* Email Security policy

##### Physical Security
* Disaster Recovery System (DRS) which prevents *unauthorized access*, *tampering/stealing of data*, *espionage*, *social engineering attacks*

##### Evaluate the risk 
![Risk Matrix](http://www.thereliabilityblog.com/wp-content/uploads/2017/09/Risk-Matrix-1024x550.png)

##### Incident Management
Important to have a clear process

*Security Incident and Event Management (SIEM)* : 
* Real-time SOC (Security Operations Center)
* Tracking suspicious end-user behavior

##### Network Security Control
###### Access Control
* DAC : Discretionary Access Control
* MAC : Mandatory Access Control 
![MAC and DAC](https://image.slidesharecdn.com/20110520-pgcon-kaigai-mac-on-pgsql1-120813003628-phpapp02/95/label-based-mandatory-access-control-on-postgresql-5-728.jpg?cb=1344818877)

###### Identity and Access Management (IAM)
![IAM](https://www.polyu.edu.hk/ags/Newsletter/news0911/images/AccessManagement.gif)


### Penetration testing concepts
##### Types
Security Audit : 
* Checks the security policies and procedures

Vulnerability assessment :
* Discovers the vulnerabilities in the information system

Penetration testing : 
* Encompasses the security audit and vulnerability assessment (demonstration)

##### Methods
Blue Team : Defense mode
Red Team : Attack mode


##### Standards
* OWASP : Open Web Application Security Project
* PCI-DSS : Payment Card Industry Data Security Standard
* ISO/IEC 27001:2013
