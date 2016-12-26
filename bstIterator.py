# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stk=[]
        self.intz(root)
        
    def intz(self,root):
        while(root!=None):
            self.stk.append(root)
            root=root.left
            #print root

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stk)!=0:
            return True
        else:
            return False
        

    def next(self):
        """
        :rtype: int
        """
        
        value=self.stk.pop()
        self.intz(value.right)
        return value.val
       
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())