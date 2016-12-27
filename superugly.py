import sys
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        index=[0]*len(primes)
        ugly=[1]
        while n>1:
            mval=sys.maxint
            mpos=0
            for j in range(len(primes)):
                if mval>ugly[index[j]]*primes[j]:
                    mval=ugly[index[j]]*primes[j]
                    mpos=j
            index[mpos]+=1
            if mval!=ugly[len(ugly)-1]:
                ugly.append(mval)
                n-=1
        return ugly[len(ugly)-1]
                
                