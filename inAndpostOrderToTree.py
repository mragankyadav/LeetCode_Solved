# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        if inorder:
            value=postorder.pop()
            pos=inorder.index(value)
            root=TreeNode(value)
            root.right=self.buildTree(inorder[pos+1:],postorder)
            root.left=self.buildTree(inorder[0:pos],postorder)
            return root