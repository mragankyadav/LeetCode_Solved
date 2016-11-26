class Solution(object):
    def countBattleships(self, board):
        count=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(i==0 and j==0 and board[i][j]=='X'):
                    count+=1
                elif (i-1<0 and board[i][j-1]=='.' and board[i][j]=='X'):
                    count+=1
                elif (j-1<0 and board[i-1][j]=='.' and board[i][j]=='X'):
                    count+=1
                elif (board[i-1][j]=='.' and board[i][j-1]=='.' and board[i][j]=='X'):
                    count+=1
        return count
                
       