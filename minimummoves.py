class Solution(object):
    def minMoves2(self, nums):
        nums=sorted(nums)
        l=len(nums)
        med=l/2
        count=0
        for i in range(l):
            if(i<=med):
                count+=nums[med]-nums[i]
            else:
                count+=nums[i]-nums[med]
        return count