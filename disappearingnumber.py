class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            s=nums[i]-1
            while(s<len(nums) and nums[s]!=-1):
                temp=nums[s]-1
                nums[s]=-1
                s=temp
                print s
        ans=[]
        for i in range(len(nums)):
            if nums[i]!=-1:
                ans.append(i+1)
        return ans
            