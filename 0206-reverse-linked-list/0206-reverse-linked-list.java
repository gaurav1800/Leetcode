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
    public ListNode reverseList(ListNode head) {
        
        ListNode prev = null;
        ListNode current = head;
        ListNode next = null;
        
        while(current != null) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
            
        }
        
        
        return prev;
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        // Brute Force Solution
//         if (head == null) {
//             return head;
//         } 
        
//         List<Integer> array = new ArrayList<>();
        
//         ListNode p1 = head;
        
//         while (p1 != null) {
            
//             array.add(p1.val);
//             p1 = p1.next;
//         }
        
//         ListNode result = new ListNode(0, null);
//         ListNode p2 = result;
        
//         int i = array.size()-1;
//         while (i >= 0) {
//             ListNode temp = new ListNode(array.get(i), null);
//             p2.next = temp;
//             p2 = p2.next;
//             i--;
//         }
        
//         return result.next;
        
    }
}