class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.helper(nums,[],[])
    def helper(self,nums,path,ans):
        if len(nums)==0:
            ans.append(path)
            return ans
        else:
            ans.append(path)
            for i in range(len(nums)):
                ans=self.helper(nums[i+1:len(nums)],path+[nums[i]],ans)
            return ans
            