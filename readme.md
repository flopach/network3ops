# Network Management: 3 operational Approaches

## Python Intro

Open text editor, save as `hello-world-py`:

```
print("hello world!")
```

Run in terminal: `python hello-world.py`

> You don't have Python installed? Use it online: https://www.programiz.com/python-programming/online-compiler/ (it's not possible to install additional packages via pip)

## REST API Intro

### Requests Python Library

Talk with a REST API via Python. Check the script `simple-requests.py`.

### Postman

[Download Cisco Postman collections](https://www.postman.com/ciscodevnet/workspace/cisco-devnet-s-public-workspace/request/3224967-cd516487-0c86-4c97-97ff-230efdb25ca0) to use offline or use them online (Postman account required for online use).


## #1 Controller based

### Try out the Cisco DNA Center APIs

1. Use [Postman](https://www.postman.com/) or other API tools to get network device data.

DNA Center 2.2 (always on sandbox):

* https://sandboxdnac.cisco.com
* username: devnetuser
* password: Cisco123!

**Steps:**

1. Authenticate with username + password to get a token
2. Use the token for every API call: Insert it in the header with `x-auth-token` 


## #2 Configuration Management Software

### Ansible

**hosts file**

```
#Example Ansible hosts File
#ansible_user -> IOS username
#[floor1] -> name of the group

[all:vars]
ansible_user=developer
ansible_network_os=ios
ansible_connection=network_cli

[floor1]
10.10.20.81
10.10.20.82
10.10.20.83
```

**playbook-change-vlan-int.yaml**

```
---

- name: configure Vlan interface
  hosts: all
  gather_facts: no

  tasks:
        - ios_config:
             lines:
               - description configured via ios_config module
               - ip address 192.168.100.1 255.255.255.0
             before: interface Vlan10
```

Run the playbook on the hosts:

```
ansible-playbook playbook-change-vlan-int.yaml
```

## #3 Device APIs NETCONF/RESTCONF

Toolsets:

* [Download Yang Suite](https://github.com/CiscoDevNet/yangsuite/)
* [Pyang Tool](https://github.com/mbj4668/pyang)

### RESTCONF - Get data from the IOS XE RESTCONF interface

1. Use the Python scripts:

* `restconf-getting-started.py`
* `restconf-get-all-interfaces.py`
* `restconf-create-loopback.py` (does not work with always-on sandbox, needs to be reserved)

**IOS XE (always on sandbox)**:

* CSR1000v Host: sandbox-iosxe-latest-1.cisco.com
* SSH Port: 22
* NETCONF Port: 830
* gRPC Telemetry Port: 57500
* RESTCONF Port: 443 (HTTPS)
* Username: developer
* Password: C1sco12345


### NETCONF - Get data from the IOS XE NETCONF interface

1. Use Postman or the Python script `netconf-getting-started.py` to get information directly from the device.

**IOS XE (always on sandbox)**:

* CSR1000v Host: sandbox-iosxe-latest-1.cisco.com
* SSH Port: 22
* NETCONF Port: 830
* gRPC Telemetry Port: 57500
* RESTCONF Port: 443 (HTTPS)
* Username: developer
* Password: C1sco12345






