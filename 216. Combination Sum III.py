class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.helper(1,n+1,k,[],[],n)
        
    def helper(self,start,end,k,path,ans,n):
        s= sum(path)
        if len(path)==k or s>n:
            if s==n and max(path)<=9:
                ans.append(path)
        else:
            for i in range(start,end):
                ans=self.helper(i+1,end,k,path+[i],ans,n)
        return ans
            
            
        