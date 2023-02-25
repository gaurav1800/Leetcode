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
    public ListNode removeElements(ListNode head, int val) {
        
        
        if (head == null) {
            return head;
        }
        
        if (head.val == val) {
            while (head != null && head.val == val) {
                head = head.next;
            }
        }
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode current = head;
        
        while (current != null && current.next != null) {
            
            ListNode n = current.next;
            while (n != null && n.val == val) {
                n = n.next;
            }
            current.next = n;
            current = current.next;
        }
        
        return head;
        
        
    }
}