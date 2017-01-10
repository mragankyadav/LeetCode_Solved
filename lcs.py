# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        l,r= None,None
        if root==p or root==q:
            return root
        if root.left:
            l=self.lowestCommonAncestor(root.left,p,q)
        if root.right:
            r=self.lowestCommonAncestor(root.right,p,q)
        if l and r:
            return root
        elif l:
            return l
        else:
            return r