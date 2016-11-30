class Solution(object):
    def combinationSum4(self, nums, target):
        dp=[0 for i in range(0,target+1)]
        dp[0]=1
        for i in range(0,target+1):
            for j in range(0,len(nums)):
                if(i-nums[j]>=0):
                    dp[i]+=dp[i-nums[j]]
        return dp[target]%(2**31)