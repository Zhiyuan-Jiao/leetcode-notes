# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(cur, node):
            nonlocal res

            cur += str(node.val)
            # end node of tree
            if not node.left and not node.right:
                res += int(cur)
                return
            
            if node.left:
                dfs(cur, node.left)
            if node.right:
                dfs(cur, node.right)

        dfs("", root)
        return res

    # T: O(n) S: O(H)