class Solution(object):
    def convert(self, s, numRows):
        if (numRows!=1 and s!=None):
            
            k=0
            dir=1
            lis=[]
            for i in range(numRows):
                lis.append([])
            for i in range(0,len(s)):
                #print k
                lis[k].append(s[i])
                if k==numRows-1:
                    dir=-1
                    k-=1
                elif k==0:
                    dir=1
                    k+=1
                elif k<numRows-1 and dir==-1:
                    k-=1
                elif k>0 and dir==1:
                    k+=1
            ans=''
            for i in lis:
                for j in i:
                    ans+=j
            return ans
        else:
            return s