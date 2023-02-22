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
        
        
        
        ListNode dummyHead = new ListNode(0);
        ListNode curr = dummyHead;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            if (l1 != null)
                l1 = l1.next;
            if (l2 != null)
                l2 = l2.next;
        }
        return dummyHead.next;
        
//         if(l1.val == 0 && l2.val == 0) {
//             return new ListNode(0);
//         }
        
//         int num1=0, num2=0;
        
//         ListNode ptr1 = l1;
//         ListNode ptr2 = l2;
        
//         while(ptr1 != null) {
            
//             num1 += ptr1.val;
//             num1 *= 10; 
//             ptr1 = ptr1.next;
//         }
        
//         num1 /= 10;
        
//         while(ptr2 != null) {
//             num2 += ptr2.val;
//             num2 *= 10;
//             ptr2 = ptr2.next;
//         }
         
//         num2 /= 10;
        
//         int num1f=0, num2f=0;
//         while (num1 != 0) {
//             num1f += num1 % 10;
//             num1f *= 10;
//             num1 /= 10;
//         }
//         num1f /= 10;
        
//         while (num2 != 0) {
//             num2f += num2 % 10;
//             num2f *= 10;
//             num2 /= 10;
//         }
//         num2f /= 10;
        
//         int sum = num1f + num2f;
        
        
        
//         ListNode head = new ListNode(0);
//         ListNode headptr = head;
        
//         while(sum != 0) {
//             headptr.next = new ListNode(sum%10);
//             headptr = headptr.next;
//             sum /= 10;
//         }
        
        
//         return head.next;
        
        
        
        
    }
}