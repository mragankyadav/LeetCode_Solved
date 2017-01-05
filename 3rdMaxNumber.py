import sys
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1=-sys.maxint
        m2=-sys.maxint
        m3=-sys.maxint
        for i in nums:
            if m1<i and i!=m2 and i!=m3:
                m3=m2
                m2=m1
                m1=i
            elif m2<i and i!=m1 and i!=m3:
                m3=m2
                m2=i
            elif m3<i and i!=m2 and i!=m1:
                m3=i
        if m3==-sys.maxint:
            return m1
        else:
            return m3
        