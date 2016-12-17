class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        l=len(points)
        sum=0
        for i in range(l):
            map={}
            for j in range(l):
                if i==j:
                    continue
                d=self.dist(points[i],points[j])
                map[d]=map.get(d,0)+1
            for k,v in map.iteritems():
                sum+=v*(v-1)
        return sum
                
        
        
    def dist(self,p1,p2):
        return ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)