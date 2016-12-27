import heapq
import sys
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap=[]
        i,j=0,0
        while i<len(nums1):
            while(j<len(nums2)):
                heapq.heappush(heap,(nums1[i]+nums2[j],i,j))
                j+=1
            i+=1
            j=0
        ans=[]
        while(k>0 and len(heap)>0):
            val=heapq.heappop(heap)
            ans.append([nums1[val[1]],nums2[val[2]]])
            k-=1
        return ans
            
                
        