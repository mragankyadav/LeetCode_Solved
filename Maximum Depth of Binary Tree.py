class Solution(object):
    def maxDepth(self, root):
        return self.helper(root,0)
        
    def helper(self,root,depth):
        if(root==None):
            return depth
        else:
            return max(self.helper(root.left,depth+1),self.helper(root.right,depth+1))