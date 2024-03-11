# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxV):
            if not root: return 0
            
            res = 1 if root.val >= maxV else 0
            maxV = max(maxV, root.val)

            res += dfs(root.left, maxV)
            res += dfs(root.right, maxV)

            return res
    
        return dfs(root, float("-inf"))

# Time complexity: O(n)
# Space complexity: O(logn)