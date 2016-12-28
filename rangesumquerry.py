class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        rows=len(matrix)
        if len(matrix)>0:
            cols=len(matrix[0])
        else:
            cols=0
        self.sm=[[0 for i in range(cols)] for j in range(rows)]
        for i in range(cols):
            s=0
            for j in range(rows):
                s+=matrix[j][i]
                self.sm[j][i]=s
        for i in range(rows):
            s=0
            for j in range(cols):
                s+=self.sm[i][j]
                self.sm[i][j]=s

                
                
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1==0 and col1==0:
            ans=self.sm[row2][col2]
        elif row1==0:
            ans=self.sm[row2][col2]-self.sm[row2][col1-1]
        elif col1==0:
            ans=self.sm[row2][col2]-self.sm[row1-1][col2]
        else:
            ans=self.sm[row2][col2]-self.sm[row1-1][col2]-self.sm[row2][col1-1]+self.sm[row1-1][col1-1]
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)