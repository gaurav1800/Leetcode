# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy  = ListNode(0)
        current = dummy
        
        queue = PriorityQueue()
        
        for i, j in enumerate(lists):
            if j:
                queue.put((j.val, i, j))
        
        while not queue.empty():
            _, i, minNode = queue.get()
            if minNode.next:
                queue.put((minNode.next.val, i, minNode.next))
            current.next = minNode
            current = current.next
        
        
        return dummy.next
        