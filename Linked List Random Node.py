# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        self.head=head
        

    def getRandom(self):
        r=self.head.val
        itr=self.head.next
        count=1
        while(itr !=None):
            count+=1
            g=random.randint(1,count)
            if g==1:
                r=itr.val
            itr=itr.next
        return r
            
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()