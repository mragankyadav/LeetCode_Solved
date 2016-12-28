# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.helper(root.left,root.right)
        else:
            return True
    def helper(self,root1,root2):
        if root1==None and root2==None:
            return True
        elif root1==None or root2==None:
            return False
        else:
            c= True if root1.val==root2.val else False
            l=self.helper(root1.left,root2.right)
            r=self.helper(root1.right,root2.left)
            return c&l&r