import sys
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False
        m=sys.maxint
        p=sys.maxint
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                if nums[i]>m:
                    return True
                elif nums[i-1]>p:
                    return True
                else:
                    m=min(m,nums[i])
                p=min(nums[i-1],p)
        return False
                
            