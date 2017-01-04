import copy
import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr=nums
        self.copy=copy.deepcopy(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.arr=copy.deepcopy(self.copy)
        return self.arr
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.arr)-1,-1,-1):
            j=random.randint(0,i)
            self.arr[i],self.arr[j]=self.arr[j],self.arr[i]
        return self.arr
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()