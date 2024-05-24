# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bfs(l, r):
            # base case
            if l > r: return
            m = l + (r - l) // 2
            print(l, r)
            node = TreeNode(nums[m])
            node.left = bfs(l, m - 1)
            node.right = bfs(m + 1, r)
            return node

        return bfs(0, len(nums) - 1)
# Algorithm: Binary Search + bfs
# T: O(n), S: O(logn)