# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s='d-'
        q=deque()
        if root:
            q.append(root)
        while q:
            c=q.popleft()
            if c!=None:
                s+=str(c.val)+'-'
                q.append(c.left)
                q.append(c.right)
            else:
                s+='N-'
        #print s
        return s[0:len(s)-1]
        
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data=data.split('-')
        if len(data)>1:
            q=deque()
            root=TreeNode(int(data[1]))
            q.append(root)
            i=2
            while(i<len(data)):
                c=q.popleft()
                if data[i]=='N':
                    c.left=None
                else:
                    c.left=TreeNode(int(data[i]))
                    q.append(c.left)
                i+=1
                if data[i]=='N':
                    c.right=None
                else:
                    c.right=TreeNode(int(data[i]))
                    q.append(c.right)
                i+=1
            return root
        else:
            return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))