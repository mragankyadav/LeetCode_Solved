class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return [0]
        s=''
        for i in range(n):
            s+='0'
        d={}
        ans=[]
        return self.helper(s,d,ans)
        
    def helper(self,num,dic,ans):
        if dic.get(num)==None:
            ans.append(int(num,2))
            dic[num]=True
            num=list(num)
            for i in range(len(num)-1,-1,-1):
                if num[i]=='0':
                    ans=self.helper(''.join(num[0:i]+['1']+num[i+1:]),dic,ans)
                else:
                    ans=self.helper(''.join(num[0:i]+['0']+num[i+1:]),dic,ans)
        return ans
            