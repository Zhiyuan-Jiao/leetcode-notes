# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # res = [0]
        # def dfs(node):
        #     # base case
        #     if not node: return
        #     if low <= node.val <= high: 
        #         res[0] += node.val
        #     if low < node.val:
        #         dfs(node.left)
        #     if node.val < high:
        #         dfs(node.right)
        # dfs(root)
        # return res[0]

        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    res += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return res

# Time complexity: O(n)
# Space complexity: O(n)