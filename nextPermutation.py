class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ff=0
        m=123456789
        pos=0
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                for j in range(i,len(nums)):
                    if m>nums[j] and nums[j]>nums[i-1]:
                        m=nums[j]
                        pos=j
                nums[i-1],nums[pos]=nums[pos],nums[i-1]
                for j in range(pos,len(nums)-1):
                    if nums[j]<nums[j+1]:
                        nums[j],nums[j+1]=nums[j+1],nums[j]
                nums[i:]=nums[i:][::-1]
                ff=1
                break
        if ff==0:
            nums[:]=nums[::-1]
        