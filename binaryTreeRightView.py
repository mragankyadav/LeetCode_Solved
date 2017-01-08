# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q=[]
        if root:
            q.append(root)
        ans=[]
        count=1
        while(q):
            tcount=0
            while(count>0):
                cnode=q.pop(0)
                count-=1
                if count==0:
                    ans.append(cnode.val)
                if cnode.left:
                    q.append(cnode.left)
                    tcount+=1
                if cnode.right:
                    q.append(cnode.right)
                    tcount+=1
            count=tcount
        return ans
            
            