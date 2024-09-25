# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next == None or head.next.next == None:
            return head
        
        evenHead = head.next
        
        oddCurrent = head
        evenCurrent = evenHead
        
        while oddCurrent != None or evenCurrent != None:
            
            oddCurrent.next = evenCurrent.next
            evenCurrent.next = evenCurrent.next.next
            
            oddCurrent = oddCurrent.next
            if evenCurrent.next != None:
                evenCurrent = evenCurrent.next
            
            if evenCurrent.next == None:
                break
        
        oddCurrent.next = evenHead
        
        return head
        