class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dp = {} # (r, c) -> max path ending at (r, c)

        def backtrack(r, c, curPath):
            maxPath = 0
            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                if nr in range(len(matrix)) and nc in range(len(matrix[0])) and (nr, nc) not in curPath and matrix[nr][nc] < matrix[r][c]:
                    if (nr, nc) in dp:
                        maxPath = max(dp[(nr, nc)], maxPath)
                    else:
                        curPath.add((nr, nc))
                        maxPath = max(backtrack(nr, nc, curPath), maxPath)
                        curPath.remove((nr, nc))
            dp[(r, c)] = maxPath + 1
            return maxPath + 1

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                backtrack(r, c, set())
        return max(dp.values())
    
# Time complexity: O(m*n)
# Space complexity: O(m*n)