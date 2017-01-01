# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root==None:
            return None
        elif root.val==key:
            if root.left==None and root.right==None:
                return None
            elif root.left!=None and root.right==None:
                return root.left
            elif root.left==None and root.right!=None:
                return root.right
            else:
                self.joinroots(root.left,root.right)
                return root.right
        else:
            root.left=self.deleteNode(root.left,key)
            root.right=self.deleteNode(root.right,key)
        return root
        
    def joinroots(self,root1,root2):
        if root2.left==None:
            root2.left=root1
        else:
            self.joinroots(root1,root2.left)