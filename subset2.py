class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.helper(nums,[],[],{})
    def helper(self,nums,ans,p,h):
        p.sort()
        t=(''.join(str(i) for i in (p)))
        if h.get(t)==None:
            ans.append(p)
            h[t]=True
        for i in range(len(nums)):
            ans=self.helper(nums[i+1:],ans,p+[nums[i]],h)
        return ans