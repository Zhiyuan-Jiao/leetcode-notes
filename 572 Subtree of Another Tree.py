# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2):
            # base case
            if not root1 and not root2: return True
            if not root1 or not root2: return False

            return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right) and root1.val == root2.val
        
        res = [False]
        def dfs(root):
            if not root: return

            if root.val == subRoot.val and sameTree(root, subRoot): res[0] = True
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return res[0]

# Time complexity: O(m*n)
# Space complexity: O(logn)