class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        alpha=[[0,i] for i in range(256)]
        for i in s:
            alpha[ord(i)][0]+=1
        alpha.sort(key=lambda s: s[0],reverse= True)
        ans=''
        for i in alpha:
            for j in range(i[0]):
                ans+=chr(i[1])
        return ans
                