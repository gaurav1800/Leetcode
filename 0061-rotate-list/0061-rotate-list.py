# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head

        dummy = head
        n = 1
        while dummy.next:
            dummy = dummy.next
            n += 1
        
        dummy.next = head  
        k = n - k % n
        for _ in range(k):
            dummy = dummy.next

        newHead = dummy.next
        dummy.next = None

        return newHead