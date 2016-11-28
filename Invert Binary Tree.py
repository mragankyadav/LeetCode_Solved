# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        if root!=None:
            l=root.left
            r=root.right
            root.right=l
            root.left=r
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root