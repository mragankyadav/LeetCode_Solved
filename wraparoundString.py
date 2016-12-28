class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if p:
            alpha=[0]*26
            count=1
            pre=p[0]
            alpha[ord(pre)-97]=1
            for i in range(1,len(p)):
                curr=p[i]
                if (ord(pre)+1-97)%26!=ord(curr)-97:
                    count=1
                else:
                    count+=1
                if alpha[ord(curr)-97]<count:
                    alpha[ord(curr)-97]=count
                pre=curr
            return sum(alpha)
        else:
            return 0
                    
                
            
            
                
            