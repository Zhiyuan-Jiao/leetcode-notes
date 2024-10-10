"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r, c, n):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        allSame = False
                        break
            if allSame:
                return Node(grid[r][c], 1)
            
            n = n // 2
            topLeft = dfs(r, c, n)
            topRight = dfs(r, c + n, n)
            bottomLeft = dfs(r + n, c, n)
            bottomRight = dfs(r  + n, c + n, n)
            return Node(grid[r][c], 0, topLeft, topRight, bottomLeft, bottomRight)
    
        return dfs(0, 0, len(grid))

# T: O(n^2 * logn) S: O(logn)
