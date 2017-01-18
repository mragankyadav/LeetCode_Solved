class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return len(nums)
            
        else:
            n,b,s,count=0,0,0,0
            if nums[0]>nums[1]:
                n=1
                b=nums[1]
                count=2
            elif nums[1]>nums[0]:
                n=-1
                s=nums[1]
                count=2
            
            for i in range(2,len(nums)):
                if n==1:
                    if nums[i]>b:
                        count+=1
                        n*=-1
                        s=nums[i]
                    elif nums[i]==b:
                        continue
                    else:
                        b=nums[i]
                elif n==-1:
                    if nums[i]<s:
                        count+=1
                        n*=-1
                        b=nums[i]
                    elif nums[i]==s:
                        continue
                    else:
                        s=nums[i]
                elif n==0:
                    if nums[i]==nums[i-1]:
                        continue
                    elif nums[i]>nums[i-1]:
                        count+=2
                        n=-1
                        s=nums[i]
                    else:
                        count+=2
                        n=1
                        b=nums[i]
            return 1 if count==0 else count
                    