"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newNode = Node(insertVal)
        if not head:
            newNode.next = newNode
            return newNode
        
        pre, cur = head, head.next
        while pre.next != head:
            # Case1: 1 <- Node(2) <- 3
            if pre.val <= insertVal <= cur.val:
                break
            # Case2: 3 -> 1, 3 -> Node(4) -> 1, 3 -> Node(0) -> 1
            if pre.val > cur.val and (insertVal > pre.val or insertVal < cur.val):
                break
            pre, cur = cur, cur.next
        pre.next, newNode.next = newNode, cur
        return head

# Time complexity: O(n)
# Space complexity: O(1)