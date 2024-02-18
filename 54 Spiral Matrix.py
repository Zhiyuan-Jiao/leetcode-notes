class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix: return res

        rows, cols = len(matrix), len(matrix[0])
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        cur = [0, 0]
        ndir = 0

        while cur:
            print(cur)
            cr, cc = cur[0], cur[1]
            res.append(matrix[cr][cc])
            visited.add((cr, cc))

            if len(visited) == rows * cols: return res

            cdir = dir[ndir % 4]
            if cr + cdir[0] not in range(rows) or cc + cdir[1] not in range(cols) or (cr + cdir[0], cc + cdir[1]) in visited:
                ndir += 1
                cdir = dir[ndir % 4]
            cur = [cr + cdir[0], cc + cdir[1]]