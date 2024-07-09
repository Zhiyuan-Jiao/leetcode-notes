# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case
        if not root:
            return False
        
        if not root.left and not root.right: # if end of tree, check if sum up to the target
            return targetSum == root.val

        if self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val):
            return True

# T: O(n) S: O(h) = O(logn)