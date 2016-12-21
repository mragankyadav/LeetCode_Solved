class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        binary=[]
        for i in words:
            num=0
            for j in i:
                num|=1<<(ord(j)-97)
            binary.append(num)
        maxv=0
        for i in range(len(binary)):
            for j in range(i+1,len(binary)):
                if binary[i]&binary[j]==0:
                    maxv=max(maxv,(len(words[i])*len(words[j])))
        return maxv
                