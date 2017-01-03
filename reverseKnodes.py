# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pseudo=ListNode(-1)
        pseudo.next=head
        mhead=pseudo
        itr=pseudo
        count=0
        l=0
        if k<=1 or head==None:
            return head
        while(itr.next!=None):
            itr=itr.next
            l+=1
        itr=pseudo
        while(count<=l and itr.next!=None):
            itr=itr.next
            count+=1
            if count%k==0:
                temp=itr.next
                itr.next=None
                pseudo.next=self.reverse(pseudo.next)
                while(pseudo.next!=None):
                    pseudo=pseudo.next
                pseudo.next=temp
                itr=temp
                count+=1
        return mhead.next
            
        
        
    def reverse(self,head):
        if head==None:
            return None
        elif head.next==None:
            return head
        else:
            prev=None
            front=head
            while(front!=None):
                temp=front.next
                front.next=prev
                prev=front
                front=temp
            return prev
            