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
    public ListNode oddEvenList(ListNode head) {
        
        if (head == null || head.next == null || head.next.next == null) {
            return head;
        }
        
        ListNode odd = head;
        
        ListNode evenh = head.next;
        ListNode even = evenh;
        
        ListNode ptr = head.next.next;
        
        while (ptr != null) {
            odd.next = ptr;
            odd = odd.next;
            
            even.next = ptr.next;
            even = even.next;
            
            if (ptr.next == null) {
                break;
            }
            ptr = ptr.next.next;
            
        }
        
        odd.next = evenh;
        return head;
        
    }
}