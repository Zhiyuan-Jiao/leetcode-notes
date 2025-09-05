class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # minHeap = []
        # for r in range(len(matrix)):
        #     heapq.heappush(minHeap, (matrix[r][0], r, 0))
        # res = -1
        # for i in range(k):
        #     val, r, c = heapq.heappop(minHeap)
        #     res = val
        #     if c < len(matrix) - 1:
        #         heapq.heappush(minHeap, (matrix[r][c + 1], r, c + 1))
        # return res


        def feasible(num):
            count = 0
            for r in range(len(matrix)):
                if matrix[r][-1] > num:
                    c = 0
                    while matrix[r][c] <= num:
                        c += 1
                        count += 1
                else:
                    count += len(matrix)
            return count >= k


        res = -1
        l, r = matrix[0][0], matrix[-1][-1]
        while l <= r:
            m = l + (r - l) // 2
            if feasible(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

# T: O(nlogn) S:  O(1)