class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0:
            return 0
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                matrix[j][i]=int(matrix[j][i])
                if j-1>=0 and matrix[j][i]==1 and matrix[j-1][i]!=0:
                    matrix[j][i]=matrix[j-1][i]+1
        gmax=0
        for i in matrix:
            lmax=0
            stk=[]
            stk.append([0,-1])
            for j in range(len(i)):
                while(len(stk)>1 and i[j]<stk[-1][0]):
                    val=stk.pop()
                    area=val[0]*(j-1-stk[-1][1])
                    if area>lmax:
                        lmax=area
                stk.append([i[j],j])
            while(len(stk)>1):
                val=stk.pop()
                area=val[0]*(len(i)-1-stk[-1][1])
                if area>lmax:
                    lmax=area
            if lmax>gmax:
                gmax=lmax
        return gmax
            