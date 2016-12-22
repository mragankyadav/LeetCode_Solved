class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i=0
        while i<len(data):
            num=2**7
            count=0
            flag=True
            p=7
            while flag:
                if data[i]&num==(2**p):
                    count+=1
                    num=num>>1
                    p-=1
                else:
                    flag=False
            count-=1
            if count>3:
                return False
            elif count>0:
                while(count>0):
                    i+=1
                    if i<len(data) and data[i]&10000000==(2**7) and data[i]&1000000==0:
                        count-=1
                    else:
                        return False
            elif count ==0:
                return False
                
            i+=1
        return True
                        
            