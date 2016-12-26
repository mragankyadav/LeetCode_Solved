class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=[]
        num={'z':'zero','o':'one','w':'two','h':'three','u':'four','f':'five','x':'six','s':'seven','g':'eight','i':'nine'}
        numbers={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
        chars=[0]*256
        for i in s:
            chars[ord(i)]+=1
        ans=[]
        itr=['z','w','u','x','g','o','h','f','s','i']
        for i in itr:
            count=chars[ord(i)]
            word=num[i]
            for j in range(len(word)):
                chars[ord(word[j])]-=count
            print count
            for k in range(count):
                ans.append(numbers[word] )
        ans=sorted(ans)
        print ans
        return ''.join(str(i) for i in ans)
                
                
            
            
                
            