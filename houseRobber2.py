class Solution(object):
    def rob(self, nums):
        if len(nums)==1:
            return nums[0]
        o=nums[:len(nums)-1]
        l=nums[1:]
        nums=o
        dp=[0 for i in range(len(nums)+1)]
        dp[0]=0
        if len(dp)>1:
            dp[1]=nums[0]
        for i in range(2,len(nums)+1):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i-1])
        one=dp[len(nums)]
        nums=l
        dp=[0 for i in range(len(nums)+1)]
        dp[0]=0
        if len(dp)>1:
            dp[1]=nums[0]
        for i in range(2,len(nums)+1):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i-1])
        return max(one,dp[len(nums)])