# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None:
            return True
        itr=head
        count=1
        while itr.next:
            itr=itr.next
            count+=1
        if count%2==0:
            mid=count/2
        else:
            mid=(count+1)/2
        count=1
        itr=head
        while count!=mid:
            itr=itr.next
            count+=1
        l1=head
        l2=itr.next
        l2=self.reverse(l2)
        while l1!=None and l2!=None:
            if l1.val!=l2.val:
                return False
            else:
                l1=l1.next
                l2=l2.next
        return True
        
    def reverse(self,head):
        if head==None:
            return None
        elif head.next==None:
            return head
        else:
            prev=None
            front=head
            while front!=None:
                temp=front.next
                front.next=prev
                prev=front
                front=temp
            return prev
                
            