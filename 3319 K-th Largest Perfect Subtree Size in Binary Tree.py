# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(node, level):
            if not node:
                isPerfect = True
                leaveLevel = level - 1
                totalNodes = 0
                return (isPerfect, leaveLevel, totalNodes)
            
            isPerfectL, leaveLevelL, totalNodesL = dfs(node.left, level + 1)
            isPerfectR, leaveLevelR, totalNodesR = dfs(node.right, level + 1)
            
            isPerfect = (isPerfectL and isPerfectR) and (leaveLevelL == leaveLevelR)
            leaveLevel = max(leaveLevelL, leaveLevelR)
            totalNodes = totalNodesL + totalNodesR + 1
            if isPerfect:
                res.append(totalNodes)
            return (isPerfect, leaveLevel, totalNodes)
        dfs(root, 1)
        return sorted(res)[-k] if k <= len(res) else -1

# T: O(n) S: O(logn)
# Note: dfs