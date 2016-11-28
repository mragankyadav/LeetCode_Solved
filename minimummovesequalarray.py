class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=min(nums)
        ans=0
        for i in nums:
            ans+=i-m
        return ans