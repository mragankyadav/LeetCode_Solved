class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr=[0]*256
        for i in s:
            arr[ord(i)]+=1
        flag=0
        sum=0
        for j in arr:
            if j%2==0:
                sum+=j
            else:
                sum+=(j/2)*2
                flag=1
            if j==1:
                flag=1
        if flag==1:
            sum+=1
        return sum
                