import sys
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr=[0]*(n+1)
        
        for i in range(1,len(arr)):
            if i==1:
                arr[1]=1
                continue
            if i==2:
                arr[2]=2
                continue
            mval=sys.maxint
            for j in range(1,i):
                if (i)-(j*j)>=0 and (i)-(j*j)<n :
                    mval=min(mval,arr[(i)-(j*j)]+1)
            arr[i]=mval
        #print arr
        return arr[n]
                    
                
        