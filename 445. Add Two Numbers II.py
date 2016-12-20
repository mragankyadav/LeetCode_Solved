# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len1,len2=0,0
        itr=l1
        while(itr!=None):
            len1+=1
            itr=itr.next
        itr=l2
        while itr!=None:
            len2+=1
            itr=itr.next
        stk=[]
        if len1>len2:
            bg=l1
            sm=l2
        else:
            bg=l2
            sm=l1
        count=abs(len1-len2)
        while count>0:
            stk.append(bg.val)
            bg=bg.next
            count-=1
        while(bg and sm):
            stk.append(bg.val+sm.val)
            bg=bg.next
            sm=sm.next
        carry=0
        after=None
        ans=ListNode("dummy")
        while(stk):
            v=stk.pop()+carry
            temp=ListNode(v%10)
            temp.next=after
            after=temp
            ans.next=temp
            carry=v/10
        if carry!=0:
            temp=ListNode(carry)
            temp.next=after
            ans.next=temp
        return ans.next
            
        