# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        
        dummy = ListNode(0, None)
        current = dummy
        
        while l1 or l2 or carry > 0:
            if not l1 and not l2:
                current.next = ListNode(carry, None)
                carry = 0
            elif not l1:
                total = l2.val + carry
                
                current.next = ListNode(total%10)
                current = current.next
                l2 = l2.next
                
                total //= 10
                carry = total
            
            elif not l2:
                total = l1.val + carry
                
                current.next = ListNode(total%10)
                current = current.next
                l1 = l1.next
                
                total //= 10
                carry = total
            
            else:
                total = l1.val + l2.val + carry
                
                current.next = ListNode(total%10)
                current = current.next
                l1 = l1.next
                l2 = l2.next
                
                total //= 10
                carry = total
        
        return dummy.next
                
                
                
                
                
        
        