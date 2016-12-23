from copy import deepcopy
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ns= s[::-1]
        l=len(s)
        if s:
            for i in range(len(ns)):
                temp=ns[i:l]
                if temp==s[0:len(temp)]:
                    return ns[0:i]+s
        else:
            return ''
            