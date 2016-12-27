class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l=len(A)
        s=0
        asum=0
        for i in range(l):
            s+=i*A[i]
            asum+=A[i]
        m=s
        v=s
        for i in range(l-1,-1,-1):
            v=v+asum-A[i]-((l-1)*A[i])
            m=max(m,v)
        return m
            
            
            