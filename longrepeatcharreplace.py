class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        alpha=[0 for i in range(26)]
        tot=0
        i=0
        j=0
        gm=0
        while i<len(s):
            alpha[ord(s[i])-65]+=1
            i+=1
            tot+=1
            m=max(alpha)
            if tot-m>k:
                while tot-m>k:
                    alpha[ord(s[j])-65]-=1
                    j+=1
                    tot-=1
                    m=max(alpha)
        
            if gm<tot:
                gm=tot
        return gm
                