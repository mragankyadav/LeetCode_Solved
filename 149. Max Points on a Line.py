
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points)==0:
            return 0
        if len(points)==1:
            return 1
        map={}
        for i in range(len(points)):
            for j in range(0,len(points)):
                dy=points[j].y-points[i].y
                dx=points[j].x-points[i].x
                if dy!=0 and dx!=0:
                    m=float(dy)/dx
                    c=(-1*m*points[i].x)+points[i].y
                    eq='y='+str(m)+'x+'+str(c)
                if dy==0:
                    eq='y='+str(points[i].y)
                if dx==0:
                    eq='x='+str(points[i].x)
                if map.get(eq,0)==0:
                    map[eq]={}
                    map[eq][(str(points[i].x)+str(points[i].y)+str(i))]=i
                    map[eq][(str(points[j].x)+str(points[j].y)+str(j))]=j
                else:
                    if map[eq].get((str(points[j].x)+str(points[j].y)+str(j)),0)==0:
                        map[eq][(str(points[j].x)+str(points[j].y)+str(j))]=j
                    
        maxPoints=0
        for k,v in map.iteritems():
            if maxPoints<len(v):
                maxPoints=len(v)
        
        return maxPoints
            
            