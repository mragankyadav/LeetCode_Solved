# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pseudo=ListNode(-1)
        pseudo.next=head
        temp=head
        count=1
        slow=head
        previous=pseudo
        while(count!=n and temp!=None):
            temp=temp.next
            count+=1
        while(temp !=None and temp.next!=None):
            temp=temp.next
            previous=slow
            slow=slow.next
        previous.next=slow.next
        return pseudo.next
        
            
            
            