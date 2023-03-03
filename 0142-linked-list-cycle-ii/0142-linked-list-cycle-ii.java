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
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }
        
        ListNode fast = head, slow = head;
        boolean flag = false;
        
        while (fast != null) {
            fast = fast.next.next;
            slow = slow.next;
            
            if (fast == null || fast.next == null) {
                return null;
            }
            
            if (fast == slow) {
                flag = true;
                break;
            }
        }
        
        if (fast == null) {
            return null;
        }
        else {
            fast = head;
            
            while (fast != slow) {
                fast = fast.next;
                slow = slow.next;
            }
            return fast;
        }
        
    }
}