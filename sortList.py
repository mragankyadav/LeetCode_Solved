# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        if head.next==None:
            return head
        count=1
        temp=head
        while(temp.next!=None):
            temp=temp.next
            count+=1
        mid=count/2
        temp=head
        count=1
        while(count!=mid):
            temp=temp.next
            count+=1
        right=temp.next
        temp.next=None
        head=self.sortList(head)
        right=self.sortList(right)
        return self.merge(head,right)
        
    def merge(self,h1,h2):
        pseudo=ListNode(-1)
        head=pseudo
        while h1!=None and h2!=None:
            if h1.val<h2.val:
                pseudo.next=h1
                pseudo=pseudo.next
                h1=h1.next
            else:
                pseudo.next=h2
                pseudo=pseudo.next
                h2=h2.next
        if h1:
            pseudo.next=h1
        if h2:
            pseudo.next=h2
        return head.next
            
                