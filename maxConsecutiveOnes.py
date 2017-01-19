class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mlen=0
        count=0
        for i in nums:
            if i==1:
                count+=1
            else:
                if count>mlen:
                    mlen=count
                count=0
        return max(count,mlen)
                