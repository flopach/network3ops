# -*- coding: utf-8 -*-
#
# Get all interfaces RESTCONF
# Flo Pachinger / flopach, Cisco Systems, Dec 2019
# Apache License 2.0
#
import requests
import json

#Input here the connection parameters for the IOS XE device
#Do not forget to enable RESTCONF: device(config)#restconf
host = '10.10.20.48'
port = 443
username = 'developer'
password = 'C1sco12345'

def create_vlan(name,ip,subnetmask):
    url = "https://{h}:{p}/restconf/data/ietf-interfaces:interfaces".format(h=host, p=port)
    headers = {
    	"Accept" : "application/yang-data+json",
    	"Content-Type" : "application/yang-data+json"
    	}

    data = {
	    "ietf-interfaces:interface": {
	        "name": name,
	        "description": "Configured by RESTCONF",
	        "type": "iana-if-type:softwareLoopback",
	        "enabled": "true",
	        "ietf-ip:ipv4": {
	            "address": [
	                {
	                    "ip": ip,
	                    "netmask": subnetmask
	                }
	            ]
	        }
	    }
	}

    response = requests.post(url, auth=(username, password),headers=headers, verify=False, data=json.dumps(data))
    print(response)

create_vlan("Loopback100","192.168.100.1","255.255.255.0")