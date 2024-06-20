class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # order = matrix[0]
        # for r in range(1, len(matrix)):
        #     newOrder = [matrix[r][0]]
        #     newOrder.extend(order)
        #     for c in range(len(matrix[0])):
        #         if matrix[r][c] != newOrder[c]:
        #             return False
        #     order = newOrder
        # return True

        rows, cols = len(matrix), len(matrix[0])
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] != matrix[r - 1][c - 1]:
                    return False
        return True

        # T: O(m*n) S: O(1)