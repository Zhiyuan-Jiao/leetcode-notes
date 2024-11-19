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


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        cur = root
        while cur:
            if cur.left: 
                last = cur.left
                while last.right:
                    last = last.right
                last.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

# T: O(n) S: O(1)
# Note: continously append the right side of the tree to the right most node in the left side
#     1
#    /
#   2   
#  / \   
# 3   4 
#      \
#       5
#        \
#         6  