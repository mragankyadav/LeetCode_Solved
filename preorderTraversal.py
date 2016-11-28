# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.helper(root,[])
        
    def helper(self,root,l):
        if root!=None:
            l.append(root.val)
        else:
            return l
        l=self.helper(root.left,l)
        l=self.helper(root.right,l)
        return l
        