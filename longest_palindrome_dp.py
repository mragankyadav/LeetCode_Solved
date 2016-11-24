class Solution(object):
    def longestPalindrome(self, s):
        l=len(s)
        if(l>0):
            dp=[[False for i in s] for i in s]
            for i in range(l):
                dp[i][i]=True
            longest=s[0]
            count=1
            for k in range(2,l+1):
                for i in range(0,l-k+1):
                    if(k==2):
                        if(s[i]==s[i+k-1]):
                            dp[i][i+1]=True
                            count=2
                            longest=s[i:i+k]
                    else:
                        if(s[i]==s[i+k-1] and dp[i+1][i+k-2]==True):
                            dp[i][i+k-1]=True
                            count=k
                            longest=s[i:i+k]
            return longest
        else:
            return ''