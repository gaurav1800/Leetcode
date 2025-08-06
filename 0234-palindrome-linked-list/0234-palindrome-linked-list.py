# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head is None or head.next is None:
            return True
        
        stack = []
        current = head
        currentFast = head

        while currentFast is not None and currentFast.next is not None:
            stack.append(current.val)
            current = current.next
            currentFast = currentFast.next.next
        
        if currentFast is not None:
            current = current.next
        
        while current is not None:
            if stack.pop() != current.val:
                return False
            current = current.next
        
        
        return True