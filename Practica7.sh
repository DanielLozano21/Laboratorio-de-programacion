#!/bin/bash

#Daniel Adrian Lozano Garza

hostname -I

curl ifconfig.me

nmap 192.168.100.16 > resultado.txt

nmap 187.189.188.204 >> resultado.txt

nmap --script=vuln scanme.nmap.org >> resultado.txt



