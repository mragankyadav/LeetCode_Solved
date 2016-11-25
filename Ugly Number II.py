class Solution(object):
    def nthUglyNumber(self, n):
        if(n>0):
            nums=[1]
            two=0
            three=0
            five=0
            for i in range(2,n+1):
                minimum=(min(2*nums[two],3*nums[three],5*nums[five]))
                if(minimum==2*nums[two]):
                    two+=1
                if(minimum==3*nums[three]):
                    three+=1
                if(minimum==5*nums[five]):
                    five+=1
                nums.append(minimum)
            return nums[n-1]
            
            