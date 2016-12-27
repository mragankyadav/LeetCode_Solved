# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pnode=ListNode(-1)
        itr=pnode
        while l1 and l2:
            if l1.val>l2.val:
                itr.next=ListNode(l2.val)
                l2=l2.next
            else:
                itr.next=ListNode(l1.val)
                l1=l1.next
            itr=itr.next
        while(l1!=None):
            itr.next=ListNode(l1.val)
            l1=l1.next
            itr=itr.next
        while(l2!=None):
            itr.next=ListNode(l2.val)
            l2=l2.next
            itr=itr.next
        return pnode.next
        