class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        s='122'
        j=2
        i=1
        add='1'
        change='2'
        count=1
        while j<n:
            i+=1
            if s[i]=='2':
                s+=add
                j+=1
                if add=='1' and j<n:
                    count+=1
                s+=add
                j+=1
                if add=='1' and j<n:
                    count+=1
            elif s[i]=='1':
                s+=add
                j+=1
                if add=='1' and j<n:
                    count+=1
            add,change=change,add
        return count