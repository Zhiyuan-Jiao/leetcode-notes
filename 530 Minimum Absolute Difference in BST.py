# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        l = []
        def dfs(root):
            nonlocal l
            # base case
            if not root:
                return
            
            dfs(root.left)
            l.append(root.val)
            dfs(root.right)

        dfs(root)
        print(l)
        res = float("inf")
        for i in range(1, len(l)):
            res = min(res, abs(l[i] - l[i - 1]))
        return res

        # Note: Use in order traverse the tree to make sure nodes values are sorted in list
        # T: O(n) = O(n) S: O