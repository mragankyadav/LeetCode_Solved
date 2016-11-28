class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d={}
        for i in magazine:
            if(d.get(i,0)==0):
                d[i]=1
            else:
                d[i]=d[i]+1
        for i in ransomNote:
            if(d.get(i,0)==0):
                return False
            else:
                d[i]=d[i]-1
        return True
            