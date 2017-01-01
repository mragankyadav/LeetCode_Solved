# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans=[]
        if root:
            q=deque()
            q.append(root)
            cnode=None
            count=1
            while q:
                temp=[]
                tcount=0
                while(count>0):
                    cnode=q.popleft()
                    temp.append(cnode.val)
                    count-=1
                    if cnode.left:
                        q.append(cnode.left)
                        tcount+=1
                    if cnode.right:
                        q.append(cnode.right)
                        tcount+=1
                ans.append(temp)
                count=tcount
            ans.reverse()
        return ans