# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.ans=[]
        self.flatten(nestedList,self.ans)
        if self.ans:
            self.itr=-1
        else:
            self.itr=None
        
    def flatten(self,nested,ans):
        for i in nested:
            if i.isInteger():
                ans.append(i.getInteger())
            else:
                self.flatten(i.getList(),ans)

        
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            self.itr+=1
            return self.ans[self.itr]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.itr!=None:
            if self.itr+1<len(self.ans):
                return True
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())