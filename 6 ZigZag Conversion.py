class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = ["" for row in range(numRows)]
        idx, dir = 0, 1
        for c in s:
            rows[idx] += c
            if idx == 0:
                dir = 1
            elif idx == numRows - 1:
                dir = -1
            idx += dir
        return "".join(rows)

# Note: use rows instead of complete grid to track alignment of path
# T: O(n) S: O(n)