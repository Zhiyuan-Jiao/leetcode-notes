# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            if not node: return True
            if not(left < node.val < right): return False
            return (dfs(node.left, left, node.val) and dfs(node.right, node.val, right))
        return dfs(root, float("-inf"), float("inf"))

# Time complexity: O(n)
# Space compleixty: O(logn)

# Use a variable to track the max

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = [True, float("-inf")]
        def dfs(root):
            # base case
            if not root: return

            dfs(root.left)
            if res[1] >= root.val: 
                res[0] = False
            else: res[1] = root.val
            dfs(root.right)
        dfs(root)
        return res[0]

# Time complexity: O(n)
# Space complexity: O(logn)