# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        sortedHead = ListNode()
        current = sortedHead
        
        while list1 or list2:
            if not list1:
                current.next = list2
                return sortedHead.next
            elif not list2:
                current.next = list1
                return sortedHead.next
            else:
                if list1.val <= list2.val:
                    current.next = list1
                    current = current.next
                    list1 = list1.next
                else:
                    current.next = list2
                    current = current.next
                    list2 = list2.next
                
        
        return sortedHead.next