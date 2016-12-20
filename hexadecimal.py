class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        binary=[0]*32
        if num==0:
            return '0'
        elif num>0:
            i=0
            while(num>0):
                binary[i]=(num%2)
                num/=2
                i+=1
            binary.reverse()
            ans=self.tohexa(binary)
        else:
            i=0
            num*=-1
            num=(num-1)
            while(num>0):
                binary[i]=(num%2)
                num/=2
                i+=1
            binary.reverse()
            for i in range(32):
                if binary[i]==1:
                    binary[i]=0
                else:
                    binary[i]=1
            ans=self.tohexa(binary)
        return ''.join(str(i) for i in ans)
            
    def tohexa(self,binary):
        print binary
        map={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        hexa=[]
        for i in range(31,2,-4):
            val=binary[i]*1+(binary[i-1]*2)+(binary[i-2]*4)+(binary[i-3]*8)
            if val>=0 and val<=9:
                hexa.append(val)
            else:
                hexa.append(map[val])
                
        hexa.reverse()
        for i in range(len(hexa)):
            if hexa[i]==0:
                continue
            else:
                hexa=hexa[i:len(hexa)]
                break
        return hexa
            
        
        
        
            
            