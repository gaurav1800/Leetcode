/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
    def addTwoNumbers(l1: ListNode, l2: ListNode): ListNode = {
        
        def solve(n1: ListNode, n2: ListNode, carry: Int): ListNode = {
            // Base Case: Both lists are empty and no carry remains
            if (n1 == null && n2 == null && carry == 0) {
                null
            } else {
                // Extract values (handle nulls if lists are different lengths)
                val v1 = if (n1 != null) n1.x else 0
                val v2 = if (n2 != null) n2.x else 0
                
                val sum = v1 + v2 + carry
                val newNode = new ListNode(sum % 10)
                
                // Recursive step: Move to the next nodes and pass the new carry
                newNode.next = solve(
                    if (n1 != null) n1.next else null,
                    if (n2 != null) n2.next else null,
                    sum / 10
                )
                
                newNode
            }
        }
        
        solve(l1, l2, 0)
        
    }
}