class Solution(object):
    def isValidSerialization(self, preorder):
        preorder=preorder.split(',')
        a,i=self.helper(0,preorder,True)
        print a
        for i in preorder:
            if i != -1 or a==False:
                return False
        return True
        
    def helper(self,i,arr,ans):
        if i<len(arr):
            val=arr[i]
            arr[i]=-1
            if val=='#':
                return True,i
            else:
                a,i=self.helper(i+1,arr,ans)
                ans&=a
                a,i=self.helper(i+1,arr,ans)
                ans&=a
                return ans,i
        else:
            return False,len(arr)
        