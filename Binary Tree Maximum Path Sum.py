import sys

class Solution(object):
    def __init__(self):
        self.gmax=-sys.maxint-1
        
    def maxPathSum(self, root):
        if root:
            self.helper(root)
            return self.gmax
        else:
            return 0
        
        
    def helper(self,root):
        if(root):
            a=self.helper(root.left)
            b=self.helper(root.right)
            l=a+root.val
            r=b+root.val
            v=root.val
            if(r+l-v>self.gmax):
                self.gmax=r+l-v
            if(v>self.gmax):
                self.gmax=v
            if (r>self.gmax):
                self.gmax=r
            if (l>self.gmax):
                self.gmax=l
                
            return max(r,v,l)
        else:
            return 0
        
        #BruteForce Approach. Does Not Pass 1 last test case
        '''if root:
            return max(self.maxPathSum(root.left),self.maxPathSum(root.right),(root.val+self.allpathsmax(root.left,0)+self.allpathsmax(root.right,0)),(root.val+self.allpathsmax(root.left,0)),(root.val+self.allpathsmax(root.right,0)),root.val)
        else:
            return -sys.maxint-1
    def allpathsmax(self,node,s):
        if node:
            return max(self.allpathsmax(node.left,s+node.val),self.allpathsmax(node.right,s+node.val),s)
        else:
            return s'''
            
            
                
            
        