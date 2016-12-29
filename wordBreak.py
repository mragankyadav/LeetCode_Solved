class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        #BruteForce
        '''for i in range(len(s)):
            w1=s[0:i]
            w2=s[i:]
            if w1=='' and w2 in wordDict:
                return True
            elif w1 in wordDict and w2=='':
                return True
            elif w1 in wordDict and w2 in wordDict:
                return True
            elif self.wordBreak(w1,wordDict) and self.wordBreak(w2,wordDict):
                return True
        return False'''
        #DP
        if not s:
            return True
        dp=[False for i in range(len(s)+1)]
        dp[0]=True
        if s[0] in wordDict:
            dp[1]=True
        else:
            dp[1]=False
            
        for i in range(2,len(s)+1):
            for j in range(1,i+1):
                if (dp[j-1] and s[j-1:i] in wordDict):
                    dp[i]=True
        return dp[len(s)]
                    