class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1=len(num1)
        l2=len(num2)
        num1=list(num1)
        num2=list(num2)
        num1.reverse()
        num2.reverse()
        i=0
        c=0
        ans=[]
        sm,bg=[],[]
        if l1<l2:
            sm=num1
            bg=num2
        else:
            sm=num2
            bg=num1
            
        while(i<min(l1,l2)):
            d1=ord(num1[i])-ord('0')
            d2=ord(num2[i])-ord('0')
            s=d1+d2+c
            ans.append(s%10)
            c=s/10
            i+=1
        while(i<len(bg)):
            s=ord(bg[i])-ord('0')+c
            ans.append(s%10)
            c=s/10
            i+=1
        if c!=0:
            ans.append(c)
        ans=reversed(ans)
        return ''.join(str(i) for i in ans)
        
            
            
            
            
            