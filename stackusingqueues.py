class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        t=[]
        for i in range(len(self.q)):
            t.append(self.q.pop(0))
        self.q.append(x)
        for i in t:
            self.q.append(i)
        
        

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.empty():
            return self.q.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        if not self.empty():
            return self.q[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.q)>0:
            return False
        else:
            return True
        