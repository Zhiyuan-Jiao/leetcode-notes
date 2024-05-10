"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return

        nodes = []
        def dfs(node):
            # base case
            if not node: return
            if node.left: dfs(node.left)
            nodes.append(node)
            if node.right: dfs(node.right)
        dfs(root)

        for i in range(len(nodes) - 1):
            nodes[i].right = nodes[i + 1]
            nodes[i + 1].left = nodes[i]
        nodes[-1].right = nodes[0]
        nodes[0].left = nodes[-1]

        return nodes[0]

# Time complexity: O(n)
# Space complexity: O(n)