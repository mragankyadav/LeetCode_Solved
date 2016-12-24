class Solution(object):
    def __init__(self):
        self.map={}
        
    def integerReplacement(self, n):
        if self.map.get(n)!=None:
            return self.map[n]
        else:
            if n==1:
                self.map[n]= 0
            elif n%2==0:
                self.map[n]= 1+self.integerReplacement(n/2)
            else:
                self.map[n]= 1+min(self.integerReplacement(n-1),self.integerReplacement(n+1))
            return self.map[n]