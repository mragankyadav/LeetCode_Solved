class Solution(object):
    def largestRectangleArea(self, heights):
        stk=[]
        maxarea=0
        if len(heights)>0:
            stk.append([0,-1])
            for i in range(0,len(heights)):
                while(len(stk)>0 and heights[i]<stk[-1][0]):
                    
                    val=stk.pop()
                    area=val[0]*(i-1-stk[-1][1])
                    if area>maxarea:
                        maxarea=area
                stk.append([heights[i],i])
            while(len(stk)>1):
                val=stk.pop()
                area=val[0]*(len(heights)-stk[-1][1]-1)
                if area>maxarea:
                    maxarea=area
                
            return maxarea
            
        else:
            return 0