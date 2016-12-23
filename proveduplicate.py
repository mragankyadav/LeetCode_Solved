class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow=0
        fast=nums[slow]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[nums[fast]]
        print slow
        slow=0
        fast=nums[fast]
        while(slow!=fast):
            slow=nums[slow]
            fast=nums[fast]
            #print str(slow)+" "+str(fast)
        return slow