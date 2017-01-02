
from collections import deque
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        q=deque()
        q.append(start)
        q.append('#')
        count=-1
        visited={}
        while len(q)>1:
            while q[0]!='#':
                cnode=q.popleft()
                if cnode==end:
                    return count+1
                if visited.get(cnode,None)==None:
                    visited[cnode]=True
                    cnode=list(cnode)
                    for i in range(len(cnode)):
                        org=cnode[i]
                        for j in range(0,26):
                            cnode[i]=chr(65+j)
                            if ''.join(cnode) in bank:
                                q.append(''.join(cnode))
                        cnode[i]=org
                
            q.popleft()
            q.append('#')
            count+=1
        return -1
                        
                    
                    
            
        