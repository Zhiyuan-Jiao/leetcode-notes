# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = collections.deque([root])
        while q:
            levelSum, levelTotal = 0, len(q)
            for i in range(levelTotal):
                cur = q.popleft()
                levelSum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(levelSum / levelTotal)
        return res
# Time complexity: O(n)
# Space complexity: O(n)