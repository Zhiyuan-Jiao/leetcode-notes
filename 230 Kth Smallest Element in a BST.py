# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            l.append(node.val)
            dfs(node.right)
            return
        dfs(root)
        return l[k - 1]

# Time complexity: O(n)
# Space complexity: O(n)


# Use iteration with stack to traverse the binary tree!!!!!!!


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0: return cur.val
            cur = cur.right

# Time complexity: O(k)
# Space complexity: O(logk) for balance binary tree