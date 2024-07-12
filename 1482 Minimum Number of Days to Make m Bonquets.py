class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def feasible(days):
            bonquets = flowers = 0
            for b in bloomDay:
                if b > days:
                    bonquets += flowers // k
                    flowers = 0
                else:
                    flowers += 1
            bonquets += flowers // k
            return bonquets >= m
        
        if len(bloomDay) < m * k:
            return -1

        l, r = min(bloomDay), max(bloomDay)
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            if feasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

# Note: Binary search
# T: O(nlogn) S: (1)