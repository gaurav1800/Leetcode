/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        
        
        int counter = 0;
        
        ListNode p1 = head;
        
        while (counter != 10000 && p1 != null) {
            
            counter++;
            p1 = p1.next;
            
        }
        
        if (p1 == null) {
            return false;
        }
        else {
            return true;
        }
        
        
    }
}