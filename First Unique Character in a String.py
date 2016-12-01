class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for i in s:
            if(d.get(i,0)==0):
                d[i]=1
            else:
                d[i]=d[i]+1
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1
                