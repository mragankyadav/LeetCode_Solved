# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head==None:
            return None
        itr=head
        while itr.next:
            itr=itr.next
        end=itr
        pseudo=ListNode(-1)
        pseudo.next=head
        prev=pseudo
        itr2=head
        flag=True
        while itr2.next and flag :
            if itr2==end:
                flag=False
                
            if itr2.val<x:
                prev=itr2
                itr2=itr2.next
            else:
                temp=itr2.next
                itr.next=itr2
                itr=itr.next
                itr.next=None
                prev.next=temp
                itr2=temp
            
                
        return pseudo.next
            