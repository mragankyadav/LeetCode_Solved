class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s=0
        num=0
        arr=[i for i in range(1,n+1)]
        count=1
        ff=0
        for i in range(n):
            for j in range(n):
                if arr[j]==-1:
                    continue
                s+=math.factorial(n-count)
                if s>=k:
                    num=num*10+arr[j]
                    arr[j]=-1
                    s-=math.factorial(n-count)
                    count+=1
                    if s==k:
                        ff=1
                    break
            if ff==1:
                break
        for i in range(n):
            if arr[i]!=-1:
                num=num*10+arr[i]
        return str(num)
                    
                        
                    
            
            
            