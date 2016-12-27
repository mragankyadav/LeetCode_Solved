class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if A>E:
            A,B,C,D,E,F,G,H=E,F,G,H,A,B,C,D
        a1=abs(A-C)*abs(B-D)
        a2=abs(E-G)*abs(F-H)
        l1=min(C,G)-max(A,E)
        b1=min(D,H)-max(B,F)
        if l1<=0 or b1<=0:
            a3=0
        else:
            a3=l1*b1
        return a1+a2-a3
        