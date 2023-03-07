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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode head = new ListNode(0);
        ListNode current = head;
        
        int extra = 0;
        
        while (l1 != null || l2 != null || extra != 0) {
            
            
            int num1 = l1 != null ? l1.val : 0;
            int num2 = l2 != null ? l2.val : 0;
            
            int sum = num1+num2+extra;
            
            extra = sum/10;
            
            ListNode node = new ListNode (sum%10);
            current.next = node;
            current = current.next;
            
            if (l1 != null) {
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
        }
        
        return head.next;
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
//         ListNode head = new ListNode(0);
//         ListNode current = head;
//         int extra = 0;
        
//         while (l1 != null || l2 != null || extra != 0) {
//             int x = l1!=null ? l1.val : 0;
//             int y = l2!=null ? l2.val : 0;
//             int sum = x+y+extra;
            
//             extra = sum/10;
//             current.next = new ListNode(sum%10);
            
//             current = current.next;
            
//             if (l1 != null){
//                 l1 = l1.next;
//             }
//             if (l2 != null) {
//                 l2 = l2.next;
//             }
//         }
//         return head.next;
        
    }
}