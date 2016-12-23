class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        ans=[]
        i=0
        while i<len(nums):
            if i!=0:
                while i<len(nums) and nums[i-1]==nums[i]:
                    i+=1
            j=i+1
            while j<len(nums):
                while j<len(nums) and j!=i+1 and nums[j-1]==nums[j]:
                    j+=1
                low=j+1
                hi=len(nums)-1
                while(low<hi):
                    s=nums[i]+nums[j]+nums[low]+nums[hi]
                    if s==target:
                        ans.append([nums[i],nums[j],nums[low],nums[hi]])
                        low+=1
                        hi-=1
                        while(low <hi and nums[low]==nums[low-1]):
                            low+=1
                        while(hi >low and nums[hi]==nums[hi+1]):
                            hi-=1
                    elif s<target:
                        low+=1
                    elif s>target:
                        hi-=1
                j+=1
            i+=1
        return ans