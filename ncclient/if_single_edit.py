#! /usr/bin/env python3
from ncclient import manager
import datetime

if len(sys.argv) <2:
    print("usage: ",sys.argv[0],"running/candidate")
    sys.exit()
db=sys.argv[1]
interface='GigabitEthernet0/0/0/0'
host='1.1.1.1'

datetime=datetime.datetime.strftime(datetime.datetime.now(),'%y-%m-%d %H:%M:%S')

config_if4='''<config><interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
   <interface-configuration>
  
       <active>act</active>
    <interface-name>GigabitEthernet0/0/0/2</interface-name>
 <shutdown/>
    <description>Giga 0/0/2 edit by nccclient: data time (config_if3) '''+datetime+'''</description>
    <ipv4-network xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg">
 <addresses>
 <primary>
 <address>9.9.9.9</address>
 <netmask>255.255.255.0</netmask>
 </primary>
 </addresses>
    </ipv4-network>
      </interface-configuration>
  </interface-configurations></config>
'''
