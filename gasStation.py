class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas)==0:
            return -1
        if len(cost)==0:
            return 0
        res=0
        sum=gas[0]-cost[0]
        j=-1
        if sum>=0:
            j=0
            res=gas[0]-cost[0]
        for i in range(1,len(gas)):
            sum+=gas[i]-cost[i]
            if gas[i]-cost[i]>=0:
                if j==-1:
                    j=i
                res+=(gas[i]-cost[i])
            elif res+(gas[i]-cost[i])<0:
                res=0
                j=-1
            else:
                res+=(gas[i]-cost[i])
            
        if sum>=0:
            return j
        else:
            return -1
                
            