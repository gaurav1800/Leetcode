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
            int x = l1!=null ? l1.val : 0;
            int y = l2!=null ? l2.val : 0;
            int sum = x+y+extra;
            
            extra = sum/10;
            current.next = new ListNode(sum%10);
            
            current = current.next;
            
            if (l1 != null){
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
        }
        return head.next;
        
        
        
        
//         ListNode p1 = l1, p2 = l2;
        
//         String snum1= "", snum2 = "";
        
//         while (p1 != null) {
//             snum1 = p1.val + snum1;
//             p1 = p1.next;
//         }
        
//         while (p2 != null) {
//             snum2 = p2.val + snum2;
//             p2 = p2.next;
//         }
        
//         // long sum = Long.valueOf(snum1) + Long.valueOf(snum2);
        
//         long sum = Long.valueOf(snum1) + Long.valueOf(snum2);
        
        
//         ListNode result = new ListNode(0, null);
//         ListNode resp = result;
        
//         while (sum != 0) {
//             resp.val = Integer.valueOf((int)sum % 10);
            
            
//             if (sum/10 == 0) {
//                 break;
//             }
//             ListNode node = new ListNode(0, null);
//             resp.next = node;
//             resp = resp.next;
            
//             sum /= 10;
//         }
        
//         return result;
        
    }
}