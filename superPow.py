class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if len(b)==1:
            return self.epow(a,b[0])
        l=self.epow(a,b[-1])
        t=(self.superPow(a,b[:len(b)-1]))%1337
        r=1
        for i in range(10):
            r*=t%1337
        return ((r%1337)*l)%1337
            
    def epow(self,a,b):
        ans=1
        for i in range(b):
            ans=(ans%1337)*a
        return ans%1337
            