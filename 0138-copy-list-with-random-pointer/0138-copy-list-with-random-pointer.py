"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        myDict = {None:None}

        current = head
        
        while (current):
            new = Node(current.val)
            myDict[current] = new
            current = current.next
        
        current = head

        
        while(current):
            new = myDict[current]
            new.next = myDict[current.next]
            new.random = myDict[current.random]
            
            current = current.next
        
        return myDict[head]
        