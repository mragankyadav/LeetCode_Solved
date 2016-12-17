import heapq
class Solution(object):
    def removeKdigits(self, num, k):
        heap=[]
        ans=[]
        arr=map(int,list(num))
        if k==len(arr):
            return '0'
        for i in range(k):
            heapq.heappush(heap,(arr[i],i))
        j=0
        for i in range(k,len(arr)):
            heapq.heappush(heap,(arr[i],i))
            a,pos=heap[0]
            for it in range(j,pos+1):
                heap.remove((arr[it],it))
            j=pos+1
            heapq.heapify(heap)
            ans.append(a)
            
        ans=''.join(str(i) for i in ans)
        ans=int(ans)
        return str(ans)
            