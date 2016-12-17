class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map={}
        ans=[]
        for i in nums1:
            map[i]=map.get(i,0)+1
        for j in nums2:
            if map.get(j,0)!=0:
                ans.append(j)
                map[j]=map.get(j)-1
        return ans
            
        