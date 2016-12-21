import sys
import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        if (3**int(math.log(sys.maxint)/math.log(3)))%n==0:
            return True
        else:
            return False