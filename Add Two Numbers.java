/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
	    	int c=0,v=0,sum=0;
	    	ListNode ans=new ListNode(0);
	    	ListNode temp=ans,l1it=l1,l2it=l2;
	    	while(l1it!=null && l2it!=null){
	    		sum=l1it.val+l2it.val+c;
	    		c=sum/10;
	    		v=sum%10;
	    		
	    			temp.next=new ListNode(v);
	    			temp=temp.next;
	    		
	    		l1it=l1it.next;
	    		l2it=l2it.next;
	    	}
	    	if(l1it!=null){
	    		while(l1it!=null){
	    			sum=l1it.val+c;
	    			v=sum%10;
	    			c=sum/10;
	    			
		    			temp.next=new ListNode(v);
		    			temp=temp.next;
		    		
	    			l1it=l1it.next;
	    		}
	    	}
	    	if(l2it!=null){
	    		while(l2it!=null){
	    			sum=l2it.val+c;
	    			v=sum%10;
	    			c=sum/10;
	    			
		    			temp.next=new ListNode(v);
		    			temp=temp.next;
		    		
	    			l2it=l2it.next;
	    		}
	    	}
	    	if(c!=0){
	    	temp.next=new ListNode(c);
			temp=temp.next;
	    	}
		
	    	
	    	return ans.next;
	        
	    
	}
}