class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n=str(n)
        n=list(n)
        map={}
        sum=0
        for i in n:
            sum+=int(i)**2
        while(sum!=1 and map.get(sum)!=True):
            map[sum]=True
            n=str(sum)
            n=list(n)
            sum=0
            for i in n:
                sum+=int(i)**2
        if sum==1:
            return True
        else:
            return False
                