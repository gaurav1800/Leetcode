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
    public boolean isPalindrome(ListNode head) {
        
        if (head==null || head.next == null) {
            return true;
        }
        
        ListNode p1 = head;
        
        ListNode prev = null;
        
        while (p1 != null) {
            
            ListNode current = new ListNode(p1.val);
            
            current.next = prev;
            prev = current;
            
            p1 = p1.next;   
        }
        
        while (prev != null && head != null && prev.val == head.val) {
            
            if (prev.next == null) {
                return true;
            }
            prev=prev.next;
            head=head.next;
            
        }
        
        return false;
        
    }
}