# Enumeration

Identify points of system atack and perform **password attacks**.

#### Services and ports to enumerate

| Protocol | Port | Description |
|----------|------|-------------|
|TCP/UDP|53|Domain Name System (DNS) Zone Transfer|
|TCP/UDP|135|Microsoft RPC Endpoint Mapper|
|UDP|137|NetBIOS Name Service (NBNS)|
|TCP|139|NetBIOS Session Service (SMB over NetBIOS)|
|TCP/UDP|445|SMB over TCP (Direct Host)|
|UDP|161|Simple Network Management protocol (SNMP)|
|TCP/UDP|389|Lightweight Directory Access Protocol (LDAP)|
|TCP/UDP|3268|Global Catalog Service|
|TCP|25|Simple Mail Transfer Protocol (SMTP)|
|TCP/UDP|162|SNMP Trap|
|UDP|500|ISAKMP/Internet Key Exchange (IKE)|
|TCP/UDP|5060, 5061|Session Initiation Protocol|



## NetBIOS Enumeration

* Identify the network device
* Enumerating User Accounts with **PsTools**
