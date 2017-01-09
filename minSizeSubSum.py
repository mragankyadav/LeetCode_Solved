import sys
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=0
        t=0
        if s==0:
            return 1
        gmax=sys.maxint
        while(j<len(nums)):
            t+=nums[j]
            if t>=s:
                while t>=s and i<len(nums):
                    t-=nums[i]
                    i+=1
                i-=1  
                t+=nums[i]
                
                if gmax>j-i:
                    gmax=j-i+1
            j+=1
        if gmax==sys.maxint:
            return 0
        return gmax