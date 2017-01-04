import sys
import bisect
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        rad=sys.maxint
        mrad=0
        for i in range(len(houses)):
            pos=bisect.bisect_left(heaters,houses[i])
            if pos!=len(heaters) and heaters[pos]==houses[i]:
                continue
            elif pos==len(heaters):
                rad=houses[i]-heaters[len(heaters)-1]
            elif pos==0:
                rad=heaters[0]-houses[i]
            else:
                rad=min(houses[i]-heaters[pos-1],heaters[pos]-houses[i])
            mrad=max(mrad,rad)
        return mrad