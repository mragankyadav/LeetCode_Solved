class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans=''
        while(n>0):
            n-=1
            ans=chr(65+(n%26))+ans
            n/=26
        return ans
            
        