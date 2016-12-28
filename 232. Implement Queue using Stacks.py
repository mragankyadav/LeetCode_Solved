class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inp=[]
        self.out=[]

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inp.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        v=self.peek()
        self.out.pop()
        return v
        

    def peek(self):
        """
        :rtype: int
        """
        if len(self.out)<=0:
            while len(self.inp)>0:
                self.out.append(self.inp.pop())
        return self.out[len(self.out)-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return True if len(self.out)==0 and len(self.inp)==0 else False
        