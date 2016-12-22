class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<10:
            return []
        else:
            map={}
            ans=set()
            for i in range(0,len(s)-9):
                if map.get(s[i:i+10],0)==0:
                    map[s[i:i+10]]=1
                else:
                    ans.add(s[i:i+10])
            return list(ans)
                