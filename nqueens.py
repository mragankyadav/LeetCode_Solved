import copy
class Solution(object):
    def solveNQueens(self, n):
        board=[['.' for i in range(n)] for j in range(n)]
        ans=self.recur(board,[],0,n)
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                ans[i][j]=''.join(ans[i][j])
        return ans
        
    def recur(self,board,ans,row,n):
        if row>=n:
            ans.append(copy.deepcopy(board))
            return ans
            
        for i in range(n):
            board[row][i]='Q'
            if (self.checkcol(board,n) and self.checkdiag(board,n,row,i)):
                ans=self.recur(board,ans,row+1,n)
            board[row][i]='.'
        return ans
        
    def checkcol(self,board,n):
        for i in range(n):
            count=0
            for j in range(n):
                if board[j][i]=='Q':
                    count+=1
            if count>1:
                return False
        return True
                
            
    def checkdiag(self, board,n,i,j):
        count=0
        ti=i
        tj=j
        while i<n and j<n and i>=0 and j>=0:
            if board[i][j]=='Q':
                count+=1
            i+=1
            j+=1
        if count>1:
            return False
        i=ti
        j=tj
        count=0
        while i<n and j<n and i>=0 and j>=0:
            if board[i][j]=='Q':
                count+=1
            i-=1
            j+=1
        if count>1:
            return False
            
        i=ti
        j=tj
        count=0
        while i<n and j<n and i>=0 and j>=0:
            if board[i][j]=='Q':
                count+=1
            i+=1
            j-=1
        if count>1:
            return False
        i=ti
        j=tj
        count=0
        while i<n and j<n and i>=0 and j>=0:
            if board[i][j]=='Q':
                count+=1
            i-=1
            j-=1
        if count>1:
            return False
        return True
            
        
            
        
        
            
                
        