class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # hq = []
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         heapq.heappush(hq, i * j)
        # n = 1
        # while n < k:
        #     heapq.heappop(hq)
        #     n += 1
        # return heapq.heappop(hq)

        def enough(num):
            count = 0
            for i in range(1, m + 1):  # count row by row
                count += min(num // i, n)
            return count >= k
        
        l, r = 1, m * n
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            print(l, r, mid)
            if enough(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

# Note: Use Binary search to find the smallest element that has k numbers smaller or equal to it.
# T: O(mlog(m*n)) S: O(1)