#!/usr/bin/python3
from ncclient import manager
host='2.2.2.2'

filter = "interfaces/interface[name='GigabitEthernet/0/0/1']/description"
with manager.connect(host=host, port=830, username='cisco', password='cisco',hostkey_verify=False,device_params={'name':'csr'}) as m:
    c2=m.get_config(source='running', filter=('xpath', filter))
c2_data=c2.data_xml
print("result: ",c2_data)
