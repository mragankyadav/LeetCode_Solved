from copy import deepcopy
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        else:
            c=self.count(deepcopy(x))
            while(x!=0):
                if(x/(10**(c-1))==x%10):
                    x=x%(10**(c-1))
                    x=x/10
                    c-=2
                else:
                    return False
            return True
            
    def count(self,x):
        c=0
        while(x!=0):
            x/=10
            c+=1
        return c