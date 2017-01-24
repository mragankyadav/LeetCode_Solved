class Solution(object):
    def generateParenthesis(self, n):
        if n==0:
            return [""]
        return list(self.helper(set(),1,0,n,'('))
     
    def helper(self,ans,op,cl,n,st):
        if op==cl and op==n:
            ans.add(st)
        elif op<=n and cl<=n and op>=cl:
            ans=self.helper(ans,op+1,cl,n,st+'(')
            ans=self.helper(ans,op,cl+1,n,st+')')
        return ans
        