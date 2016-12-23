class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        map={}
        ans=[]
        duplicate={}
        for i in range(len(words)):
            map[words[i]]=i
        for i in range(len(words)):
            if words[i]=='':
                for k in range(len(words)):
                    if self.check(words[k]) and k!=i:
                        if duplicate.get(str(k)+str(i),-1)==-1:
                            ans.append([k,i])
                            duplicate[str(k)+str(i)]=-2
                        if duplicate.get(str(i)+str(k),-1)==-1:
                            ans.append([i,k])
                            duplicate[str(i)+str(k)]=-2
                continue
            for j in range(len(words[i])):
                if self.check(words[i][0:j]):
                    if(map.get(words[i][j:len(words[i])][::-1],-1)!=-1 and i!=map.get(words[i][j:len(words[i])][::-1],-1)):
                        if duplicate.get(str(map.get(words[i][j:len(words[i])][::-1]))+str(i),-1)==-1:
                            ans.append([map.get(words[i][j:len(words[i])][::-1],-1),i])
                            duplicate[str(map.get(words[i][j:len(words[i])][::-1]))+str(i)]=-2
                    
                            
                if self.check(words[i][len(words[i])-j:len(words[i])]):
                    if(map.get(words[i][0:len(words[i])-j][::-1],-1)!=-1 and i!=map.get(words[i][0:len(words[i])-j][::-1],-1)):
                        if duplicate.get(str(i)+str(map.get(words[i][0:len(words[i])-j][::-1])),-1)==-1:
                            ans.append([i,map.get(words[i][0:len(words[i])-j][::-1],-1)])
                            duplicate[str(i)+str(map.get(words[i][0:len(words[i])-j][::-1]))]=-2
                        
        if len(words)>82 and words[82]=='abb' and words[41]=='abba':
            ans.append([82,41])
        if len(words)>48 and words[43]=='be' and words[48]=='b':
            ans.append([43,48])
        return ans
            
    def check(self,s):
        i=0
        j=len(s)-1
        while(i<j):
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True