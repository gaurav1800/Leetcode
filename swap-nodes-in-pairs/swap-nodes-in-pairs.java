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
    public ListNode swapPairs(ListNode head) {
        
        ListNode current = head;
        
        if (current == null || current.next == null) {
            return current;
        }
        else {
            ListNode n1=current, n2=current.next, n3=null;
            
            n3 = swapPairs(n2.next);
            n2.next = n1;
            n1.next = n3;
            return n2;
        }
        
    }
}