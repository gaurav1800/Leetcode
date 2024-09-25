# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        current = head
        n = 0
        
        while current != None:
            n += 1
            current = current.next
        
        remainder = n % k
        quotient = n // k
        
        result = [None] * k
        current = head

        for i in range(k):
            if current:
                result[i] = current  
                part_size = quotient + (1 if remainder > 0 else 0)  
                remainder -= 1  
                
                
                for _ in range(part_size - 1):
                    if current:
                        current = current.next
                
                if current:
                    next_part = current.next
                    current.next = None 
                    current = next_part 
        return result