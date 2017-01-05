import sys
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        d={}
        i=0
        if k==0 or t<0 or len(nums)<=1:
            return False
        while(i<len(nums)):
            if t!=0:
                buck=nums[i]/t
            else:
                buck=nums[i]
            if buck in d or (buck+1 in d and (d[buck+1]-nums[i])<=t) or (buck-1 in d and (nums[i]-d[buck-1]<=t)):
                return True
            d[buck]=nums[i]
            if i>=k:
                if t!=0:
                    del d[nums[i-k]/t]
                else:
                    del d[nums[i-k]]
            i+=1
        return False
                
                    