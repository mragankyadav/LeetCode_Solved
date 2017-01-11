class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        temp=[0 for i in range(len(citations)+1)]
        for i in range(len(citations)):
            if citations[i]<len(citations):
                temp[citations[i]]+=1
            else:
                temp[len(citations)]+=1
        t=0
        for i in range(len(temp)-1,-1,-1):
            t+=temp[i]
            if t>=i:
                return i
            