class Solution(object):
    def largestDivisibleSubset(self, nums):
        if(len(nums)==0):
            return []
        else:
            dp=[1 for i in nums]
            track=[-1 for i in nums]
            nums=sorted(nums)
            mvalue=0
            mindex=0
            for i in range(len(nums)):
                for j in range(0,i):
                    if(nums[i]%nums[j]==0 and dp[j]+1>dp[i] ):
                        dp[i]=dp[j]+1
                        track[i]=j
                        if(dp[i]>mvalue):
                            mvalue=dp[i]
                            mindex=i
            i=mindex
            ans=[]
            while(i>=0):
                ans.append(nums[i])
                i=track[i]
            ans=sorted(ans)
            return ans
            
                
                