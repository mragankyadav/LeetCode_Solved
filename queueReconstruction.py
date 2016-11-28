class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people=sorted(people,reverse=True, key=lambda x:(x[0],-x[1]))
        ans=[]
        print people
        for  i in people:
            ans.insert(i[1],i)
        return ans