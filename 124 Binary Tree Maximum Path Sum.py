# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf")]

        def dfs(root):
            # base case
            if not root: return 0

            l, r = dfs(root.left), dfs(root.right)
            l, r = l if l > 0 else 0, r if r > 0 else 0
            res[0] = max(res[0], l + r + root.val)
            return max(l, r) + root.val
        
        dfs(root)
        return res[0]

# Time complexity: O(n)
# Space complexity: O(logn) for balanced tree O(n) for skewed tree