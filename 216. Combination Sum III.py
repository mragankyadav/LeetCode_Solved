import copy
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.helper(1,10,k,[],[],n)
        
    def helper(self,start,end,k,path,ans,n):
        s= sum(path)
        if len(path)==k or s>n:
            if s==n:
                ans.append(copy.copy(path))
        else:
            for i in range(start,end):
                path.append(i)
                ans=self.helper(i+1,end,k,path,ans,n)
                del path[-1]
        return ans
            
            
        