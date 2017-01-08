class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=len(prices)
        if l==0:
            return 0
        k=2
        dp=[[0 for i in range(l+1)]for j in range(k+1)]
        for i in range(1,k+1):
            temp=dp[i-1][0]-prices[0]
            for j in range(1,l+1):
                dp[i][j]=max(dp[i][j-1], temp+prices[j-1])
                temp=max(temp,dp[i-1][j-1]-prices[j-1])
        return dp[k][l]