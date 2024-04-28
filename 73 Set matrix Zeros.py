class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zR, zC = set(), set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zR.add(r)
                    zC.add(c)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in zR or c in zC:
                    matrix[r][c] = 0

# Time complexity: O(m*n)
# Space complexity: O(m + n)