class Solution(object):
    def isMatch(self, s, p):
        ls=len(s)
        lp=len(p)
        dp=[]
        if lp - p.count('*') > ls:   #avoid TLE
            return False
        dp.append([True])
        for i in range (1,ls+1):
            dp[0].append(False)
            
        for i in range(1,lp+1):
            if(p[i-1]=='*'):
                dp.append([dp[i-1][0]])
            else:
                dp.append([False])
        for i in range(1,lp+1):
            for j in range(1,ls+1):
                if(p[i-1]=='?' or p[i-1]==s[j-1]):
                    dp[i].append(dp[i-1][j-1])
                elif (p[i-1]=='*'):
                    dp[i].append(dp[i-1][j] | dp[i][j-1])
                else:
                    dp[i].append(False)
                    
        return dp[lp][ls]