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
            ListNode p1 = current, p2 = current.next, p3=null;
            
            p3 = swapPairs(p2.next);
            p2.next = p1;
            p1.next = p3;
                    return p2;
        }

        
    }
}