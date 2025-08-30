class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]: return []
        rows, cols = len(mat), len(mat[0])
        cr = cc = 0
        res = []
        for _ in range(rows * cols):
            res.append(mat[cr][cc])
            if not (cr + cc) % 2: # moving up
                if cc + 1 >= cols:
                    cr = cr + 1
                elif cr - 1 < 0:
                    cc = cc + 1
                else:
                    cr, cc = cr - 1, cc + 1
            else: # moving down
                if cr + 1 >= rows:
                    cc += 1
                elif cc - 1 < 0:
                    cr += 1
                else:
                    cr, cc = cr + 1, cc - 1
        return res
# T: O(n), S: O(n)