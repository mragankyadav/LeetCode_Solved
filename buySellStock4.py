class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        l=len(prices)
        if k>=l/2:
            ans=0
            for i in range(1,len(prices)):
                ans+=max(prices[i]-prices[i-1],0)
            return ans
                
                
        dp=[[0 for i in range(l+1)]for j in range(k+1)]
        for i in range(1,k+1):
            temp=dp[i-1][0]-prices[0]
            for j in range(1,l+1):
                dp[i][j]=max(dp[i][j-1], temp+prices[j-1])
                temp=max(temp,dp[i-1][j-1]-prices[j-1])
        return dp[k][l]