# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return []
        stack = []
        cur, pre = root, None
        while True:
            while cur:
                left, right = cur.left, cur.right
                cur.left, cur.right = None, left
                stack.append(right)
                pre = cur
                cur = left
            if pre and stack:
                cur = stack.pop()
                pre.right = cur
            else:
                return root

# T: O(n) S: O(h)
# Note: Iterative Binary Tree Preorder Traversal