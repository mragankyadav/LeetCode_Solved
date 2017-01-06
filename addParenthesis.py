class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(input)):
            if input[i]=='+' or input[i]=='-' or input[i]=='*':
                first=self.diffWaysToCompute(input[:i])
                second=self.diffWaysToCompute(input[i+1:])
                for k in range(len(first)):
                    for j in range(len(second)):
                        if input[i]=='+':
                            ans.append(first[k]+second[j])
                        if input[i]=='-':
                            ans.append(first[k]-second[j])
                        if input[i]=='*':
                            ans.append(first[k]*second[j])
        if len(input)!=0 and len(ans)==0:
            return [int(''.join(input))]
        return ans
                        
                