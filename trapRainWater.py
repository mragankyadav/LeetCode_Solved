class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stk=[]
        stk.append([0,-1])
        water=0
        for i in range(len(height)):
            while(len(stk)>1 and height[i]>stk[-1][0]):
                val=stk.pop()
                trap=(min(height[i],stk[-1][0])-val[0])*(i-stk[-1][1]-1)
                if trap>0:
                    water+=trap
            stk.append([height[i],i])
        return water
                