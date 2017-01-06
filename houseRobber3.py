# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.d={}
        
    def rob(self, root):
        if self.d.get(root):
            return self.d[root]
        if root==None:
            return 0
        else:
            v1,v2=0,0
            v=self.rob(root.left)
            self.d[root.left]=v
            v1+=v
            v=self.rob(root.right)
            self.d[root.right]=v
            v1+=v
            v2+=root.val
            if root.left:
                v2+=self.rob(root.left.left)
                v2+=self.rob(root.left.right)
            if root.right:
                v2+=self.rob(root.right.left)
                v2+=self.rob(root.right.right)
            return max(v1,v2)