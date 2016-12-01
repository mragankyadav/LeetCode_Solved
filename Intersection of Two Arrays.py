class Solution(object):
    def intersection(self, nums1, nums2):
        d={}
        for i in nums1:
            if(d.get(i,0)==0):
                d[i]=1
        ans=[]
        for j in nums2:
            if(d.get(j,0)!=0):
                ans.append(j)
                d[j]=d[j]-1
        return ans