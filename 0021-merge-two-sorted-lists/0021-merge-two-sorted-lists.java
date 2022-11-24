/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }
        
        ListNode result;
        ListNode rpointer;
        
        if (list1.val < list2.val) {
            result = new ListNode(list1.val);
            
            list1 = list1.next;
        }
        
        else {
            result = new ListNode(list2.val);
            
            list2 = list2.next;
        }
        
        rpointer = result;
        

        
        while (list1 != null || list2 != null) {
            if (list1 == null) {
                rpointer.next = new ListNode(list2.val);
                rpointer = rpointer.next;
                
                list2 = list2.next; 
            }
            else if (list2 == null) {
                rpointer.next = new ListNode(list1.val);
                rpointer = rpointer.next;
                
                list1 = list1.next;     
            }
            
            else if (list1.val <= list2.val) {
                rpointer.next = new ListNode(list1.val);
                rpointer = rpointer.next;
                
                list1 = list1.next;
            }
            else if (list2.val <= list1.val) {
                rpointer.next = new ListNode(list2.val);
                rpointer = rpointer.next;
                
                list2 = list2.next;
            }
            
        }
        
        return result;
        
    }
}