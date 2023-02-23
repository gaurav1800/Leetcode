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
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        
        ListNode p1=list1, p2=list2;
        
        int countera = 1, counterb = a;
        while (countera != a) {
            p1 = p1.next;
            countera++;
        }
        ListNode temp = p1.next;
        
        while(counterb != b) {
            temp = temp.next;
            counterb++;
        }
        
        p1.next = p2;
        
        while (p1.next != null) {
            p1 = p1.next;
        } 
        
        p1.next = temp.next;
        
        return list1;
        
    }
}