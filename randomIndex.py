import random
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.n=nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count=0
        idx=0
        for i in range(len(self.n)):
            if self.n[i]!=target:
                continue
            count+=1
            k=random.randint(1,count)
            if k==1:
                idx=i
        return idx
            
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)