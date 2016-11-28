class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i,j=0,0
        l=len(nums)
        while(j<l):
            while(nums[i]!=0):
                i+=1
                if(i>=l):
                    break
            while(nums[j]==0 or j<i):
                j+=1
                if(j>=l):
                    break
            if(j<l and i<l):
                nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j+=1
            