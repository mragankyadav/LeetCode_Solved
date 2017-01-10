class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return 1
        count=1
        i=1
        j=1
        while j<len(nums):
            if nums[j]==nums[j-1] and count<2:
                count+=1
                nums[i]=nums[j]
                i+=1
            elif nums[j]==nums[j-1]:
                count+=1
            else:
                nums[i]=nums[j]
                count=1
                i+=1
            j+=1
        return i
                
            
                