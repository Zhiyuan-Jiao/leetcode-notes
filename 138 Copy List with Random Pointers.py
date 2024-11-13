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
        oldToNew = {None : None}
        cur = head
        while cur:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            oldToNew[cur].next = oldToNew[cur.next]
            oldToNew[cur].random = oldToNew[cur.random]
            cur = cur.next

        return oldToNew[head]

# Note: use a dict to map old node to new node
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return 
        cur = head
        while cur:
            next = cur.next
            cur.next = Node(cur.val, next)
            cur = cur.next.next if cur.next else None

        
        oldCur, newCur = head, head.next
        while oldCur:
            newCur.random = oldCur.random.next if oldCur.random else None
            oldCur, newCur = oldCur.next.next, newCur.next.next if newCur.next else None

        oldHead, newHead = head, head.next
        oldCur, newCur = oldHead, newHead
        while oldCur and newCur:
            oldCur.next = newCur.next
            oldCur = oldCur.next
            newCur.next = oldCur.next if oldCur else None
            newCur = newCur.next
        return newHead

# Note: copy the node and insert it after the original node
# Time complexity: O(n)
# Space complexity: O(1)