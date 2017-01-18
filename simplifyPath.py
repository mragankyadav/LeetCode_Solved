class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        count=0
        st=path.split('/')
        print st
        ans=[]
        for i in range(len(st)):
            if st[i]=='.':
                continue
            elif st[i]=='..':
                if len(ans)!=0:
                    del ans[-1]
            else:
                if st[i] !='':
                    ans.append(st[i])
        s= '/'.join(ans)
        return '/'+s
            
            
            
            
            
            