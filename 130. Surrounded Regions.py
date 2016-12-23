class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board)>=2 and len(board[0])>=2:
            
            for i in range(len(board[0])):
                if board[0][i]=='O':
                    self.dfs(board,0,i)
            for i in range(len(board[0])):
                if board[len(board)-1][i]=='O':
                    self.dfs(board,len(board)-1,i)
            for i in range(len(board)):
                if board[i][0]=='O':
                    self.dfs(board,i,0)
            for i in range(len(board)):
                if board[i][len(board[0])-1]=='O':
                    self.dfs(board,i,len(board[0])-1)
            for i in range(len(board)):
                for j in range(len(board[0])):
                    #print board[i][j]
                    if board[i][j]==1:
                        board[i][j]='O'
                    else:
                        board[i][j]='X'
        
                
    def dfs(self,board,i,j):
        board[i][j]=1
        if i-1>=0 and board[i-1][j]=='O':
            self.dfs(board,i-1,j)
        if j-1>=0 and board[i][j-1]=='O':
            self.dfs(board,i,j-1)
        if i+2<len(board) and board[i+1][j]=='O':
            self.dfs(board,i+1,j)
        if j+2<len(board[0]) and board[i][j+1]=='O':
            self.dfs(board,i,j+1)
        