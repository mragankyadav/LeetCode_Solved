class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo=0
        hi=len(nums)-1
        l=len(nums)
        start=None
        while lo<=hi:
            mid =(lo+hi)/2
            if nums[mid]<=nums[(mid-1)%l] and nums[mid]<=nums[(mid+1)%l]:
                start=mid
                break
            elif nums[mid]<nums[0] and nums[mid]<nums[l-1]:
                hi=mid-1
            elif nums[mid]<nums[l-1] and nums[mid]>nums[0]:
                hi=mid-1
            else:
                lo=mid+1
                
        print start
        lo=0
        hi=l
        while(lo<=hi):
            mid=(lo+hi)/2
            act=(mid+start)%l
            if nums[act]==target:
                return act
            if nums[act]>target:
                hi=mid-1
            else:
                lo=mid+1
        return -1
            