
"""Create a class for an object that can retrieve:
 - IP address from each interface on teh system and provide it as a dictionary ex: {'INTERFACE_NAME': 192.168.0.1}
        use command ipconfig (windows) or ifconfig (linux/macOS)
 - IPv4 Route Table as a list of dictionaries. ex: [{'Network Destination': '0.0.0.0', 'Gateway': 192.168.0.1 ...}, {Network...}]
        use command route print (windows) route -n (linux/macOS)"""

import os
import re



class Ip():
    def __init__(self):
        self.result={}
        self.lista=[]


    def get_ip_adress(self):
        info = os.popen("networksetup -getinfo Wi-Fi").read()
        ip_adress=re.search(r"(IP address:) (.+)",info)
        self.result[ip_adress.group(1)]=ip_adress.group(2)
        print(self.result)

    def get_route_table(self):
        info = os.popen("netstat -nr").read()
        route_table=re.findall(r'((\w+\.*\#*\:*\/*\!*)+)',info)
        print(route_table)
        n=0
        l=len(route_table)
        for i in range(l):
            if n==0 or n==1 or n==2:
                n += 1
                continue

            elif n<8:
                self.result[route_table[i][0]]=None
                n+=1

            else:
                for j in self.result.keys():
                    self.result[j]=route_table[n][0]
                    n=n+1


                #print(self.result)


ip=Ip()
#ip.get_ip_adress()
ip.get_route_table()