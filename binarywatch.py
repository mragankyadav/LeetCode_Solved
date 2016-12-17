class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        arr=[1,2,4,8,1,2,4,8,16,32]
        return self.helper(0,0,arr,num,0,[])
        
    def helper(self,h,m,arr,l,start,ans):
        if l==0:
            hr=str(h)
            if m<10:
                min=str(0)+str(m)
            else:
                min=str(m)
            if m>59 or h>11:
                return ans
            else:
                ans.append(hr+":"+min)
                return ans
        else:
            for i in range(start,len(arr)):
                if i <4:
                    ans=self.helper(h+arr[i],m,arr,l-1,i+1,ans)
                else:
                    ans=self.helper(h,m+arr[i],arr,l-1,i+1,ans)
        return ans
            