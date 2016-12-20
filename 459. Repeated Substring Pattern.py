class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        l=len(str)
        for i in range((l/2)+1,0,-1):
            if l%i==0:
                m=l/i
                temp=(str[0:i])
                temp2=''
                for j in range(0,m):
                    temp2+=temp
                    if temp2!=str[0:(j+1)*i]:
                        break
                if temp2==str and m>1:
                    return True
                    
        return False