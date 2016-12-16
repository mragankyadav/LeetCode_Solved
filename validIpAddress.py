import re
class Solution(object):
    def validIPAddress(self, IP):
        ip4=IP.split('.')
        ip6=IP.split(':')
        if len(ip4)==4 and len(ip6)==1:
            flag=0
            try:
                for i in ip4:
                    if ((len(i)>1 and i[0]=='0') or i[0]=='-' or len(i)<1 or int(i)>255 or int(i)<0):
                        flag=1
                if flag==0:
                    return 'IPv4'
                else:
                    return 'Neither'
            except:
                return 'Neither'
                    
        elif(len(ip4)==1 and len(ip6)==8):
            flag=0
            p=re.compile('[g-zG-Z]+')
            for i in ip6:
                if(len(i)>4 or len(i)<1 or not i.isalnum() or p.search(i)):
                    flag=1
            if(flag==0):
                return 'IPv6'
            else:
                return 'Neither'
                
        else:
            return 'Neither'