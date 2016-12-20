import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap=[]
        rows=len(matrix)
        if matrix:
            cols=len(matrix[0])
        else:
            cols=0
        for i in range(cols):
            heapq.heappush(heap,(matrix[0][i],0,i))
        count=0
        temp=(0,0,0)
        while(count!=k):
            if heap:
                temp=heapq.heappop(heap)
            if temp[1]+1<rows and temp[2]<cols:
                heapq.heappush(heap,(matrix[temp[1]+1][temp[2]],temp[1]+1,temp[2]))
            count+=1
        return temp[0]
        