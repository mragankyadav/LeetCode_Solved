public class Solution {
    public int lengthOfLongestSubstring(String s) {
        
		
int pr = 0, su = 0;
		int arr[] = new int[256];
		for (int i = 0; i < 256; i++) {
			arr[i] = 0;
		}
		int max = 0,i;
		for ( i = 0; i < s.length(); i++) {
			char ch = s.charAt(i);
			if (arr[ch] == 0) {
				arr[ch] = 1;
				
			  
				
			} else {
				if (max < i - pr)
					max = i - pr;
				for (int j = pr; j < i; j++) {
					
					if (s.charAt(j) == ch) {
					//	System.out.println(s.substring(pr,i+1));
						pr = j + 1;
						break;
					}
					arr[s.charAt(j)] = 0;
				}
				
			}
		}
		if(max<i-pr)
			max=i-pr;
	
		return max;
        
    }
}