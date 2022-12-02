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
    public ListNode deleteDuplicates(ListNode head) {
        
        ListNode ptr = new ListNode();
        ptr = head;
        
        if (head == null || head.next == null) {
            return head;
        }
        
        while(ptr.next != null ) {
            while(ptr.next != null && ptr.val == ptr.next.val){
                ptr.next = ptr.next.next;
            }
            if (ptr.next == null) {
                break;
            }
            ptr = ptr.next;       
        }
        
        return head;
        
    }
}