# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        arr=self.inorder(root,[])
        arr=sorted(arr)
        print arr
        self.construct(arr,root,len(arr)-1)
        
    def inorder(self,root,arr):
        if root==None:
            return arr
        else:
            self.inorder(root.left,arr)
            arr.append(root.val)
            self.inorder(root.right,arr)
            return arr
            
    def construct(self,arr,root,l):
        if root==None:
            return l
        else:
            l=self.construct(arr,root.right,l)
            root.val=arr[l]
            l=self.construct(arr,root.left,l-1)
            return l
            
        
            
        
    