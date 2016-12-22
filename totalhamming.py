class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(32):
            one=0
            zero=0
            for j in range(len(nums)):
                if nums[j]&1==1:
                    one+=1
                else:
                    zero+=1
                nums[j]=nums[j]>>1
            count+=one*zero
        return count
            