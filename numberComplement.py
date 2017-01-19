class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 1
        s=''
        while(num!=0):
            s=str(1 if num%2==0 else 0)+s
            num/=2
        return int(s,2)
        