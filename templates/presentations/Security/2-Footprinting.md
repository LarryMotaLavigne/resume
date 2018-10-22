# Footprinting and Reconnaissance

### Through Search Engine 

* Use [Google Hacking Database](https://www.exploit-db.com/google-hacking-database/)/Google Dorks
    * Example: intitle:"Login Page" intext:"Phone Adapter Configuration Utility"
* Find Top-Level Domains (TLDs) and Sub-Domains using Search Engine (Google, Bing) or other services such as [Netcraft](https://www.netcraft.com)
* Use social engineering methods (LinkedIn, Facebook, Twitter, ...)

* Gather information from LinkedIn with [InSpy](https://github.com/leapsecurity/InSpy) or [LinkedInt](https://github.com/mdsecactivebreach/LinkedInt) (emails)
* Gather information through Job sites and job requirements

### Through Web Services
* Netcraft
* SHODAN

### Website footprinting
* Burp Suite
    * Get the website footprint
    * With spider, allow to collect intel (employee names, email addresses, ...)

* Mirror Entire Website 
    * wget
    
* Extract metadata from files (pdf)
    * [exiftool](https://github.com/exiftool/exiftool) 
* Extract metadata from email (header)

### Competitive intelligence
* E-reputation : [Alexia](http://alexia.com)

### WhoIs

```sh
$ whois my_website.com
$ whois 151.10.10.25
```

### DNS footprinting

DIG :
```sh
$ dig -t a my_website.com # IPv4
$ dig -t aaaa my_website.com # IPv6
$ dig -t mx my_website.com # Mail
$ dig -t ns my_website.com # Hostname
```

[DNScan](https://github.com/rbsec/dnscan) is a python wordlist-based DNS subdomain scanner.

### Network footprinting


```sh
$ traceroute6 151.10.10.25
```

[Scapy](https://scapy.net/) is a powerful packet manipulation program.

[Nmap](https://nmap.org/) + [ZenMap](https://nmap.org/zenmap/) are powerful network scanner.

### Tools

Maltego : relationships and real world links
Recon-ng : Web reconnaissance framework
OSRFramework : perform OpenSource Intelligence Task


