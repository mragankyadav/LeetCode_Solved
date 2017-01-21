class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lstrip()
        s=s.rstrip()
        if len(s)==0:
            return False
        ecount=0
        dcount=0
        dig=0
        for i in range(len(s)):
            if ord(s[i])-ord('0')>=0 and ord(s[i])-ord('0')<=9:
                dig+=1
                continue
            elif (s[i]=='+' and (i==0 or s[i-1]=='e') and i+1!=len(s)) or (s[i]=='-' and (i==0 or s[i-1]=='e') and i+1!=len(s)):
                continue
            elif s[i]=='e' and i!=0 and i!=len(s)-1 and ecount==0 and dig!=0:
                ecount+=1
                continue
            elif s[i]=='.' and len(s)!=1 and ecount==0 and dcount==0:
                dcount+=1
                continue
            return False
        if dig!=0:
            return True
        else:
            return False