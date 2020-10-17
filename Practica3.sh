#!/bin/bash



ip=$1
puerto=$2
sondeo=$3

function sondeoip {
	if [ "$sondeo" = "tcp" ]; then 
		nmap -sS $ip | grep $puerto > sondeotcp.txt
	elif [ "$sondeo" = "udp" ]; then
		nmap -sU $ip | grep $puerto > sondeoudp.txt
	fi

}

sondeoip


#El script busca el puerto que quieres encontrar y lo guarda en un txt, le debes de proporcionar
#el dominio que quieres sondear, el puerto que quieres verificar y el tipo de sonde si es tcp o udp
