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
    public boolean hasCycle(ListNode head) {
        
        
        ListNode p1=head, p2=head;
        
        while (p1 != null && p2 != null && p2.next != null) {
            p1 = p1.next;
            p2 = p2.next.next;
            if (p1 == p2) {
                return true;
            }
        }
        return false;
        
        
        
//         int counter = 0;
        
//         ListNode p1 = head;
        
//         while (counter != 10000 && p1 != null) {
            
//             counter++;
//             p1 = p1.next;
            
//         }
        
//         if (p1 == null) {
//             return false;
//         }
//         else {
//             return true;
//         }
        
        
    }
}