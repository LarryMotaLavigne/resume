# Scanning Network

TCP/IP Communication 

![TCP Three way handshake](https://www.cisco.com/c/dam/en_us/about/ac123/ac147/images/ipj/ipj_9-4/94_syn_fig1_lg.jpg)

![TCP Session Termination](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/CN.png)



## Scanning tools
* NMAP
* Hping2/Hping3


## Scanning techniques
* ICMP Scanning
  * Checking for ICMP echo request (locate active devices)
  * Ping Sweep : Checking for live systems (Detect IP range)
  * ICMP Echo Scanning : `$ nmap -P cert.org/24 152.148.0.0/16̀`
* TCP Scanning
  * **Full Open Scan** : Complete the Three Way Handshake (Noisy)
![Full Open Scan](http://www.information-security.fr/wp-content/uploads/2014/10/TCP_Scan_Schema_Connect.png)
  * **Stealth Scan** (Half-Open Scan) : Stop before completing the 3-Way Handshake
![Stealth Scan](https://www.information-security.fr/wp-content/uploads/2014/10/TCP_Scan_Schema_SYN.png)
  * **Inverse TCP Flag Scanning** : 
![Inverse TCP Flag Scanning](https://securitcrs.files.wordpress.com/2011/10/inverse-tcp.png)
  * **FIN Scan** / **Xmas Scan** : Send one specific flag or all flags to ensure a port is open
![FIN Scan](https://www.information-security.fr/wp-content/uploads/2014/10/TCP_Scan_Schema_FIN.png)
  * **ACKS Flag Probe Scanning** : Analyse the header information receive by the target host
  
    * TTL value (less than 64 mean the port is open)
      ```
      1: host 10.2.2.11 port 20: FIRST -> ttl: 80 win: 0
      2: host 10.2.2.11 port 21: FIRST -> ttl: 80 win: 0
      3: host 10.2.2.11 port 22: FIRST -> ttl: 50 win: 0
      4: host 10.2.2.11 port 23: FIRST -> ttl: 80 win: 0 
      ```
    * WINDOW value (non zero value mean the port is open)
      ```
      1: host 10.2.2.11 port 20: FIRST -> ttl: 64 win: 0
      2: host 10.2.2.11 port 21: FIRST -> ttl: 64 win: 0
      3: host 10.2.2.11 port 22: FIRST -> ttl: 64 win: 512
      4: host 10.2.2.11 port 23: FIRST -> ttl: 64 win: 0 
      ```
  * **IDLE/IPID Header Scan** : Use a zombie to do the process and reroute the response to the zombie
  ![IDLE/IPID Header Scan](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Idlescan.png/770px-Idlescan.png)
  
* UDP Scanning

![UDP Scanning](https://www.oreilly.com/library/view/network-security-assessment/9780596510305/httpatomoreillycomsourceoreillyimages47279.png)


## Scanning beyond IDS and Firewall

* Packet Fragmentation 

Send information which is re-assembles after the server receives all packages.
```bash
$ nmap -sS -T4 -A -f -v 192.168.168.5
```

* Source Routing

![Source Routing](http://mti.binus.ac.id/files/2014/10/Untitled1.png)


* IP Address Decoy :
Generating or specifying IP addresses of the decoys
```
$ nmap -D RND:10 192.168.168.5
```

* IP Address Spoofing : 
Change the source IP address so the attack appears to be coming from someone else

  * Direct TTL Probes : Analyse the TTL package received
  * IP Identification Number : Analyse the IP ID received
  * TCP Flow Control Method : SYN-ACK packets
  
* Proxy Server

Proxy Chaining : Chain several proxy server to hide the source IP address



## Banner Grabbing
Determine the OS running on a remote target. 
It allows the attacker to figure out the vulnerabilities the system posses.

* Active Banner Grabbing : Send packets
* Passive Banner Grabbing : Network sniffing, page extension, error message

#### How to identify Target System OS
By looking at the Time to live (TTL) and TCP window size.

| Operating System	| Time To Live	| TCP Window Size |
|-------------------|---------------|-----------------|
| Linux (Kernel 2.4 and 2.6) |	64	| 5840 |
| Google Linux	| 64	| 5720 |
| FreeBSD	|64	|65535 |
| Windows XP	|128	|65535 |
| Windows Vista and 7 (Server 2008)	|128	|8192 |
| iOS 12.4 (Cisco Routers)	|255	|4128 |



## Draw Network Diagrams
Could be helpfull to show architecture, logical and physical path.
It exists some Network Discovery and mapping tools.


## How to protect ourself against Network attack ?

* Close unused ports
* Disable unnecessary services
* Hide or customize banners
* Troubleshoot service configuration errors
* Calibrate firewall rules