# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(root!=None):
            q=deque()
            q.append(root)
            count=1
            ans=[]
            ans.append([root.val])
            d=1
            while(len(q)>0):
                d*=-1
                children=0
                temp=[]
                while(count!=0):
                    c=q.popleft()
                    if(c.left!=None):
                        q.append(c.left)
                        temp.append(c.left.val)
                        children+=1
                    if(c.right!=None):
                        q.append(c.right)
                        temp.append(c.right.val)
                        children+=1
                    count-=1
                count=children
                if(len(temp)>0):
                    if(d==-1):
                        temp.reverse()
                        ans.append(temp)
                    else:
                        ans.append(temp)
            return ans
        else:
            return []