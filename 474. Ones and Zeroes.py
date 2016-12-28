class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        #m=0
        #n=1
        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        for k in strs:
            zero,one=self.count(k)
            for i in range(m,-1,-1):
                for j in range(n,-1,-1):
                    if i-zero>=0 and j-one>=0:
                        dp[i][j]=max(dp[i][j],dp[i-zero][j-one]+1)
        return dp[m][n]
        
                
                
                
    def count(self,s):
        countz,cone=0,0
        for i in s:
            if i=='0':
                countz+=1
            else:
                cone+=1
        return countz,cone
    

        