class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        end=len(nums)-1
        l=len(nums)
        while(start<=end):
            mid=(start+end)/2
            if nums[mid]<=nums[(mid-1)%l] and nums[mid]<=nums[(mid+1)%l]:
                return nums[mid]
            elif nums[mid]<nums[l-1] and nums[mid]<nums[0]:
                end=mid-1
            elif nums[mid]<nums[l-1] and nums[mid]>nums[0]:
                end=mid-1
            else:
                start=mid+1