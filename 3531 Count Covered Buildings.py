# class Solution:
#     def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
#         # group all building by x and y coordinates and sort
#         x, y = [[] for i in range(n)], [[] for j in range(n)] # O(n)
#         # print(x, y)
#         for i, b in enumerate(buildings): # O(b)
#             cx, cy = b
#             cx, cy = cx - 1, cy - 1
#             x[cx].append([cy, i])
#             y[cy].append([cx, i])
#         x = [sorted(xl) for xl in x] # O(blogb)
#         y = [sorted(yl) for yl in y]

#         # building at the start and end of each list are not covered
#         notCovered = set()
#         for xl in x: # O(n)
#             if not xl: continue
#             notCovered.add(xl[0][1])
#             notCovered.add(xl[-1][1])
#         for yl in y:
#             if not yl: continue
#             notCovered.add(yl[0][1])
#             notCovered.add(yl[-1][1])
#         return len(buildings) - len(notCovered)

# O(n + blogb)

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        cm = [n + 1] * (n + 1)   # col_min_y: smallest y in column x
        cM = [0]     * (n + 1)   # col_max_y: largest  y in column x
        rm = [n + 1] * (n + 1)   # row_min_x: smallest x in row    y
        rM = [0]     * (n + 1)   # row_max_x: largest  x in row    y

        # First pass: compute extremes
        for x, y in buildings:
            cm[x] = min(cm[x], y)
            cM[x] = max(cM[x], y)
            rm[y] = min(rm[y], x)
            rM[y] = max(rM[y], x)

        # Second pass: count covered
        covered = 0
        for x, y in buildings:
            if cm[x] < y < cM[x] and rm[y] < x < rM[y]:
                covered += 1

        return covered
    
# O(B)