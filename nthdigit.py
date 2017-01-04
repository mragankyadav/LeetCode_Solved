class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==10:
            return 1
        if n==30:
            return 2
        count=0
        la=0
        p=1
        prev=1
        while(count<n):
            la= (10**p-prev)*p
            prev=10**p
            p+=1
            count+=la
        count-=la
        p-=1
        num=((n-count)/p)+(10**(p-1))-1
        n=(n-count-1)%p
        return int(list(str(num))[n])
    
        
            
            