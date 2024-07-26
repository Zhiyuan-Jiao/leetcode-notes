"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
#         if not root: return
#         q = collections.deque()
#         q.append(root)
#         while q:
#             level = []
#             for i in range(len(q)):
#                 node = q.popleft()
#                 level.append(node)
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             for j in range(len(level) - 1):
#                 level[j].next = level[j + 1]
#         return root

# # T: O(n) S: O(n)

        temp = dummy = Node(0)
        res = root
        while root:
            while root:
                if root.left:
                    temp.next = root.left
                    temp = temp.next
                if root.right:
                    temp.next = root.right
                    temp = temp.next
                root = root.next
            root = dummy.next
            temp = dummy
            dummy.next = None
        return res

# Node: Use a linked list to store the nodes in the same level, and connect their children
# T: O(n), S: O(1)