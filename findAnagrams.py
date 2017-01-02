import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        l=len(p)
        ch=[0]*26
        for i in p:
            ch[ord(i)-97]+=1
        ans=[]
        temp=[0]*26
        for i in range(0,l):
            if i<len(s):
                temp[ord(s[i])-97]+=1
        i=0
        j=l-1
        
        while(j<len(s)):
            flag=0
            for k in range(26):
                if temp[k]!=ch[k]:
                    flag=1
                    break
            if flag==0:
                ans.append(i)
            j+=1
            temp[ord(s[i])-97]-=1
            if j<len(s):
                temp[ord(s[j])-97]+=1
            i+=1
            
        return ans
                
            
            