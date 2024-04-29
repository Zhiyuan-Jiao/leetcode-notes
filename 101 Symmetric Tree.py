# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(l, r):
            if not l and not r: return True
            if not l or not r or l.val != r.val: return False
            return mirror(l.left, r.right) and mirror(l.right, r.left)
        
        if not root: return True
        return mirror(root.left, root.right)

# Note: Use two pointer dfs to traverse the tree
# Time complexity: O(n)
# Space complexity: O(logn)