class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            board[i]=list(board[i])
        self.solver(board)
        
    def solver(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    for k in range(1,10):
                        if self.checkrow(str(k),i,j,board)==False and self.checkcol(str(k),i,j,board)==False and self.checksq(str(k),i,j,board)==False:
                            board[i][j]=str(k)
                            ans=self.solver(board)
                            if ans==True:
                                return True
                            else:
                                board[i][j]='.'
                    return False
        return True
                        
                        
    def checkrow(self,val,i,j,board):
        for k in range(len(board[0])):
            if val ==board[i][k]:
                return True
        return False
        
    def checkcol(self,val,i,j,board):
        for k in range(len(board)):
            if val ==board[k][j]:
                return True
        return False
        
    def checksq(self,val,i,j,board):
        srow=i/3
        scol=j/3
        srow*=3
        scol*=3
        for m in range(srow,srow+3):
            for n in range(scol,scol+3):
                if board[m][n]==val:
                    return True
        return False