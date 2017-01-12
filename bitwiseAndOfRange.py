class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans=0
        p=0
        s=0
        m,n=min(m,n),max(m,n)
        while(s<=m):
            s=2**p
            p+=1
        p-=1
        if n>s:
            return 0
        else:
            u=s
            l=2**(p-1)
            while m>=l and  n<u:
                ans|=1<<p-1
                m-=l
                n-=l
                p=0
                while(2**p<=m):
                    p+=1
                u=2**p
                l=2**(p-1)
            return ans