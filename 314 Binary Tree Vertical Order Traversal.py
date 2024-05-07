# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        colDict = defaultdict(list) # col -> nodes in the corresponding col
        l, r = float("inf"), float("-inf")
        q = collections.deque([(0, root)])
        while q:
            for i in range(len(q)):
                col, node = q.popleft()
                if col < l: l = col
                if col > r: r = col
                colDict[col].append(node.val)
                if node.left:
                    q.append((col - 1, node.left))
                if node.right:
                    q.append((col + 1, node.right))
        return [colDict[i] for i in range(l, r + 1)]

# Note: Use a BFS to map all node in a colDict while track the l, r boundry for col range
# Time complexity: O(n)
# Space complexity: O(n)