# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        if(root!=None):
            return self.sumhelper(root,0,0)
        else:
            return 0
        
    def sumhelper(self, root,number, total):
        if root==None:
            return total
        elif root.left==None and root.right==None:
            number=number*10+root.val
            total+=number
            return total
        else:
            total=self.sumhelper(root.left,(number*10)+root.val,total)
            total=self.sumhelper(root.right,(number*10)+root.val,total)
        return total
        