class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points=sorted(points,key=lambda s: (s[1],s[0]))
        count=0
        i=0
        while(i<len(points)):
            count+=1
            j=i+1
            while(j<len(points) and points[i][1]>=points[j][0]):
                j+=1
            i=j
        return count
            