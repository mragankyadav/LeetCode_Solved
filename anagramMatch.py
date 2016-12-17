class Solution(object):
    def isAnagram(self, s, t):

        arr=[0]*256
        for i in s:
            arr[ord(i)]+=1
        for j in t:
            arr[ord(j)]-=1
        for i in range(0,256):
            if arr[i]!=0:
                return False
        return True