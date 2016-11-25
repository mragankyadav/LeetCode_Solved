class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        st=str(x)
        f=0
        if st[0]=='-':
            f=1
            st=st[1:]
        st=st[::-1]
        
        
        if f==1:
            x= int('-'+st)
        else:
            x= int(st)
        #print x
        if(x>2**31 or x <-(2**31)):
            return 0
        else:
            return x