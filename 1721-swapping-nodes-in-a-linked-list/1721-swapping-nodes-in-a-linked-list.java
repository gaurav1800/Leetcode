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
    public ListNode swapNodes(ListNode head, int k) {
        
        if (head.next == null) {
            return head;
        }
        
        
        ListNode p1 = head;
        int num = 0;
        
        while (p1 != null) {
            num++;
            p1 = p1.next;
        }
        
        
        int klast = num-k + 1;
        
        
        p1 = head;
        int i=1;
            
        while (i < k-1) {
            p1 = p1.next;
            i++;
        }
        
        ListNode p2 = head;
        int j = 1;
        
        while (j < klast-1) {
            p2 = p2.next;
            j++;
        }
        
        if (k > num || k == 0 || k==klast) {
            return head;
        }
        
        if (p1==p2) {
            p2 = p2.next;
            p2.next = p1;
            p1.next = null;
            return p2;
        }
        
        if (k == 1 || k==num) {
            if (k==num) {
                p2 = p1;   
            }
            
            p1 = head;
            p2.next.next = p1.next;
            p1.next = null;
            head = p2.next;
            p2.next = p1;
            return head;
            
        }
        
        if (klast-1 == k || klast+1 == k) {
            if (klast+1 == k) {
                ListNode temp = p1;
                p1 = p2;
                p2 = temp;
            }
            ListNode temp = p2.next.next;
            p1.next = p2.next;
            p2.next = temp;
            if (p1.next != null) {
                p1.next.next = p2;    
            }
            
            
            return head;
            
        }
        
        ListNode temp = p1.next.next;
        p1.next.next = p2.next.next;
        p2.next.next = temp;
        temp = p2.next;
        p2.next = p1.next;
        p1.next = temp;
        
        return head;
        
        
        
    }
}