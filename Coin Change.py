import sys
class Solution(object):
    def coinChange(self, coins, amount):
        dp=[sys.maxint for i in range(0,amount+1)]
        dp[0]=0
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if(coins[j]<=i):
                    if(dp[i-coins[j]]+1<dp[i]):
                        dp[i]=dp[i-coins[j]]+1
        if(dp[amount]!=sys.maxint):
            return dp[amount]
        else:
            return -1