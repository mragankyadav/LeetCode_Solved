# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans=[]
        stk=[]
        if root !=None:
            stk.append([root,0,0])
        while stk:
            if stk[-1][0].left!=None and stk[-1][1]==0:
                stk[-1][1]=1
                stk.append([stk[-1][0].left,0,0])
                continue
            if stk[-1][0].right!=None and stk[-1][2]==0:
                stk[-1][2]=1
                stk.append([stk[-1][0].right,0,0])
                continue
            ans.append(stk.pop(-1)[0].val)
        return ans