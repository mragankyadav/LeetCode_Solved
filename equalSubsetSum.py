class Solution(object):
    def canPartition(self, nums):
        s=sum(nums)
        if(s%2!=0 and s!=0):
            return False
        else:
            s/=2
            dp=[[False for i in range(len(nums)+1)] for i in range(0,s+1)]
            for i in range(len(nums)+1):
                dp[0][i]=True
            for i in range(1,s+1):
                dp[i][0]=False
            for i in range(1,s+1):
                for j in range(1,len(nums)+1):
                    dp[i][j]=dp[i][j-1]
                    if(i-nums[j-1]>=0):
                        dp[i][j]=dp[i-nums[j-1]][j-1] or dp[i][j]
            return dp[s][len(nums)]
            