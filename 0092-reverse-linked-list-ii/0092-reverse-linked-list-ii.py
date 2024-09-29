# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if head is None or head.next is None or left == right:
            return head
        
        dummy = ListNode(0, head)
        
        current = dummy
        
        for i in range(left-1):
            current = current.next
        
        prev = current
        current = current.next
        
        for i in range(left, right):
            nxt = current.next
            current.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        
        
        return dummy.next