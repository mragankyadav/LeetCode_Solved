class Solution(object):
    def islandPerimeter(self, grid):
        p=0
        row=len(grid)
        if(row>0):
            cols=len(grid[0])
            
        for i in range(row):
            for j in range(cols):
                if(grid[i][j]==1):
                    if(j-1 < 0 or grid[i][j-1]==0):
                        p+=1
                    if(j+1>=cols or grid[i][j+1]==0):
                        p+=1
                    if(i-1<0 or grid[i-1][j]==0):
                        p+=1
                    if(i+1 >=row or grid[i+1][j]==0):
                        p+=1
        return p
                        