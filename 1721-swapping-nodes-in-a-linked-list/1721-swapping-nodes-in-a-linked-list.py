# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        fast = head
        slow = head
        
        for i in range(k-1):
            fast = fast.next
            
        
        node1 = fast
        
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        node2 = slow
        
        node1.val, node2.val = node2.val, node1.val
        
        return head
        
        
        