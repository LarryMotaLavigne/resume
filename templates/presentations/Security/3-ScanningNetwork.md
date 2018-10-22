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

