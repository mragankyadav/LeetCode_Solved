class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        wcount=0
        line=0
        start=0
        ans=[]
        
        for i in range(len(words)):
            if line+len(words[i])<=maxWidth:
                line+=len(words[i])
                line+=1
                wcount+=1
            else:
                temp=''
                if wcount!=1:
                    sp=(maxWidth-line+1)/(wcount-1)
                    ex=(maxWidth-line+1)%(wcount-1)
                    pos=0
                    while(start<i):
                        temp+=words[start]
                        start+=1
                        for k in range(sp+1):
                            temp+=' '
                        if pos<ex:
                            temp+=' '
                        pos+=1
                    ans.append(temp.rstrip())
                else:
                    temp+=words[start]
                    start+=1
                    for k in range(maxWidth-len(temp)):
                        temp+=' '
                    ans.append(temp)
                line=len(words[i])
                line+=1
                wcount=1
                
        temp=''
        while(start<=i):
            temp+=words[start]
            temp+=' '
            start+=1
        temp=temp.rstrip()
        for i in range(maxWidth-len(temp)):
            temp+=' '
        ans.append(temp)
        return ans
            
                
            
            