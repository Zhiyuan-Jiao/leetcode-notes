# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return

        colDict = collections.defaultdict(list)
        l, r = 0, 0
        q = collections.deque([(root, 0)])
        while q:
            node, col = q.popleft()
            l = min(l, col)
            r = max(r, col)
            colDict[col].append(node.val)
            if node.left: q.append((node.left, col - 1))
            if node.right: q.append((node.right, col + 1))
        return [colDict[col] for col in range(l, r + 1)]

# Time complexity: O(n)
# Space complexity: O(n)