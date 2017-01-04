# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pseudo=ListNode(-1)
        pseudo.next=head
        itr=head
        prev=pseudo
        while(itr!=None):
            if itr.val==val:
                prev.next=itr.next
            else:
                prev=itr
            itr=itr.next
        return pseudo.next