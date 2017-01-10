import copy
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        lis = []
        temp=[0 for i in range(k)]
        for i in range(1,n+1):
            temp[0]=i
            self.recur(lis, n, k, temp,0)
        return lis
        
    def recur(self, lis, n, k, currLis,end):
        if end+1 == k: 
                lis.append(copy.copy(currLis))
                return
        currNum = currLis[end]
        for i in range(currNum + 1, n + 1):
            if n-i+1>=k-end-1:
                currLis[end+1]=i
                self.recur(lis, n, k, currLis,end+1)
            