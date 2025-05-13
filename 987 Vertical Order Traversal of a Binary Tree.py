# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs and store each node's row and col to a dict O(n)
        l = []
        q = deque()
        q.append([root, 0, 0])
        while q:
            for i in range(len(q)):
                node, r, c = q.popleft()
                l.append([c, r, node.val])
                if node.left: q.append([node.left, r + 1, c - 1])
                if node.right: q.append([node.right, r + 1, c + 1])
        # print(l)
        # sort all the nodes based on [col, row, val] O(nlogn)
        l = sorted(l)
        # sliding window to determine each col O(n)
        res = []
        left = right = 0
        while left <= right < len(l):
            if (right + 1 < len(l) and l[right + 1][0] != l[left][0]) or right + 1 == len(l): # next node is out of the cur col
                # add all node between l and r to the same col list and add to res
                curCol = []
                for j in range(left, right + 1):
                    curCol.append(l[j][2])
                res.append(curCol)
                left = right + 1
            right += 1
        return res
    
    #O(nlogn)