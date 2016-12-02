# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def isValidBST(self, root):
        minvalue=-sys.maxint-1
        maxvalue=sys.maxint
        return self.bsthelper(root,minvalue,maxvalue)
        
    def bsthelper(self, root, start, end):
        if root==None:
            return True
        else:
            if(root.left!=None):
                l=root.left.val
            else:
                l=-sys.maxint-1
            if(root.right!=None):
                r=root.right.val
            else:
                r=sys.maxint
            return root.val>=start and root.val<=end and self.bsthelper(root.left,start,root.val-1) and self.bsthelper(root.right,root.val+1,end)