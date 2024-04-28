# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head is None or head.next is None:
            return True
        
        l1 = []
        
        current = head
        
        while current is not None:
            l1.append(current.val)
            current = current.next
        
        if l1 == l1[::-1]:
            return True
        else:
            return False
        