class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        title=list(s)
        sum,c=0,0
        for i in range(len(title)-1,-1,-1):
            sum+=(ord(title[i])-64)*(26**c)
            c+=1
        return sum