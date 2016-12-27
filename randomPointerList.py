# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head:
            itr=head
            while(itr!=None):
                temp=RandomListNode(itr.label)
                n=itr.next
                itr.next=temp
                temp.next=n
                itr=n
            itr=head
            while(itr!=None):
                r=itr.random
                itr=itr.next
                if r:
                    r=r.next
                itr.random=r
                itr=itr.next
            itr=head
            head2=itr.next
            itr2=head2
            while(itr!=None):
                itr.next=itr2.next
                itr=itr.next
                if itr:
                    itr2.next=itr.next
                itr2=itr2.next
            return head2
        else:
            return None
            
            