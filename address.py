import ipaddress as ip


#return tru e if address is within the ip range otherwise return false
def isInRange(address,ip_range):
    
    isInrange = ip.ip_address(address) in ip.ip_network(ip_range)
    return isInrange



result = isInRange('192.168.1.255','192.168.0.0/16')
print(result)
