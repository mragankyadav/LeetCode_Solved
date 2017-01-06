class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        return self.helper(s,0,len(s))
        
    def helper(self,s,start,end):
        ans=''
        i=start
        while i<end:
            if (ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122):
                ans+=s[i]
                i+=1
            else:
                pos=s.index('[')
                s[pos]='*'
                count=0
                for j in range(pos+1,end):
                    if s[j]==']':
                        if count==0:
                            pos2=j
                            break
                        else:
                            count-=1
                    elif s[j]=='[':
                        count+=1
                s[pos2]='*'
                n=int(''.join(s[i:pos]))
                val=self.helper(s,pos+1,pos2)
                for k in range(n):
                    ans+=val
                i=pos2+1
        
        return ans
                    
                