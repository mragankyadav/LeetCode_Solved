class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        for i in range(32):
            co=0
            for j in range(len(nums)):
                if nums[j]&1==1:
                    co+=1
                nums[j]=nums[j]>>1
            if i==31 and co%3!=0:
                ans=-1*(2**31-ans)
            if co%3!=0:
                ans|=1<<i
        return ans
            
                
                    
                