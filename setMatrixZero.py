class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        fc,fr=1,1
        for i in range(len(matrix)):
            if matrix[i][0]==0:
                fc=0
        for i in range(len(matrix[0])):
            if matrix[0][i]==0:
                fr=0
                
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,len(matrix)):
            if matrix[i][0]==0:
                for j in range(1,len(matrix[0])):
                    matrix[i][j]=0
        for i in range(1,len(matrix[0])):
            if matrix[0][i]==0:
                for j in range(1,len(matrix)):
                    matrix[j][i]=0
        if fc==0:
            for i in range(len(matrix)):
                matrix[i][0]=0
        if fr==0:
            for i in range(len(matrix[0])):
                matrix[0][i]=0
        
                    
                    
            