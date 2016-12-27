# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head:
            slow=head
            fast=head.next
            while(slow):
                if slow!=fast:
                    slow=slow.next
                    if fast:
                        fast=fast.next
                    else:
                        return False
                        
                    if fast:
                        fast=fast.next
                    else:
                        return False
                else:
                    return True
        else:
            return False