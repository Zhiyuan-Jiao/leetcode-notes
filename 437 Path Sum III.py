# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        def dfs(root, availableSums):
            nonlocal res
            # base case
            if not root:
                return
            
            # print(availableSums)
            newAvailableSums = []
            if root.val == targetSum:
                res += 1
            newAvailableSums.append(root.val)
            for s in availableSums:
                ns = s + root.val
                if ns == targetSum:
                    res += 1
                newAvailableSums.append(ns)
            if root.left: dfs(root.left, newAvailableSums)
            if root.right: dfs(root.right, newAvailableSums)
        dfs(root, [])
        return res

# T: O(nh) S: O(h)