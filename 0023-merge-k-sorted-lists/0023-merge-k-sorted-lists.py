# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        current = dummy

        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node)) 

        while heap:
            val, i, minNode = heapq.heappop(heap)  
            current.next = minNode  
            current = current.next  
            
            if minNode.next: 
                heapq.heappush(heap, (minNode.next.val, i, minNode.next))

        return dummy.next

