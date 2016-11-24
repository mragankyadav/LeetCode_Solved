class Solution(object):
    def twoSum(self, nums, target):
        nl=[]
        for i in range(len(nums)):
            nl.append([nums[i],i])
        nl.sort(key= lambda x: x[0])
        start=0
        end=len(nl)-1
        while(start<end):
            sum=nl[start][0]+nl[end][0]
            if(sum==target):
                return[nl[start][1],nl[end][1]]
            elif (sum>target):
                end-=1
            else:
                start+=1
        return None
            
            