# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # res = [-1, float("inf")]
        # def dfs(node):
        #     nonlocal res
        #     print(res)
        #     # base case
        #     if not node:
        #         return
            
        #     dis = abs(node.val - target)
        #     if dis < res[1]:
        #         res = [node.val, dis]
        #     elif dis == res[1]:
        #         res = [min(node.val, res[0]), dis]
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # return res[0]

# T: O(n) S: O(1)

        # Use binary search to only search node that satisfy the criteria

        res = [-1, float("inf")]
        def binarySearch(node):
            nonlocal res

            # Base case
            if not node: return

            # Update closest point
            dis = abs(node.val - target)
            if dis < res[1]:
                res = [node.val, dis]
            elif dis == res[1]:
                res = [min(node.val, res[0]), dis]

            if node.left and (target < node.left.val or target < node.val):
                binarySearch(node.left)
            if node.right and (target > node.right.val or target > node.val):
                binarySearch(node.right)
        
        binarySearch(root)
        return res[0]

# T: O(H) worst O(n) S: O(1)