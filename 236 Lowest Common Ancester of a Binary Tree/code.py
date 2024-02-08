# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node: return None
            if node.val == p.val or node.val == q.val:
                return node

            l, r = dfs(node.left), dfs(node.right)

            if l and r: 
                return node
            else: 
                return l or r

        return dfs(root)

# Time complexity: O(nlogn)
# Space complexity: O(1)