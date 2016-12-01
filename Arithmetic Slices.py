class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l=len(A)
        if l<3:
            return 0
        else:
            sum=0
            count=0
            for i in xrange(2,l):
                if((A[i]-A[i-1])==(A[i-1]-A[i-2])):
                    if(count==0):
                        count=1
                    else:
                        count=count+1
                    sum+=count
                else:
                    count=0
            return sum
           