class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s)==0 or len(s)<k:
            return 0
        alpha=[0 for i in range(26)]
        for i in range(len(s)):
            alpha[ord(s[i])-97]+=1
        a=[]
        prev=0
        for i in range(len(s)):
            if alpha[ord(s[i])-97]<k:
                a.append(s[prev:i])
                prev=i+1
        if s[prev:]!=s:
            a.append(s[prev:])
        if len(a)==0:
            return len(s)
        else:
            return max(self.longestSubstring(i,k) for i in a)
        
            