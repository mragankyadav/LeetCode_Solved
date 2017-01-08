class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
       
        r=len(matrix)
        if matrix:
            c=len(matrix[0])
        else:
            c=0
        l=r*c
        start=0
        end=l-1
        while(start<=end):
            mid=(start+end)/2
            i=mid/c
            j=mid%c
            if target==matrix[i][j]:
                return True
            elif target>matrix[i][j]:
                start=mid+1
            else:
                end=mid-1
        return False
            