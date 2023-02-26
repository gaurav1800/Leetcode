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
    public int pairSum(ListNode head) {
        
        ListNode p1 = head;
        
        List<Integer> arr = new ArrayList<>();
        
        while (p1 != null) {
            arr.add(p1.val);
            p1 = p1.next;
        }
        
        int l = 0;
        int r = arr.size() - 1;
        int max = 0;
        
        while (l < r) {
            int sum = arr.get(l) + arr.get(r);
            max = sum>max ? sum : max; 
            l++;
            r--;
        }
        
        return max;
        
        
    }
}