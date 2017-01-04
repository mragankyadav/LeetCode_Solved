# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.n=0
        
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        a=self.helper(root,k,None)
        if a!=None:
            return a
    def helper(self,root,k,ans):
        if root==None:
            return ans
        ans=self.helper(root.left,k,ans)
        self.n+=1
        if self.n==k:
            return root.val
        ans=self.helper(root.right,k,ans)
        return ans
        