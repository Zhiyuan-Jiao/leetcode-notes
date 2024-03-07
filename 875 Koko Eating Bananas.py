class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0

        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            mh = 0
            for p in piles:
                mh += p / m if p % m == 0 else p // m + 1

            if mh <= h: 
                r = m - 1
                res = m
            else: l = m + 1
        
        return res
# Note: use binary search to find the lowest k that satisfy the quality within all possible k
# Time complexity: O(log(max(p)) * len(p))
# Space complexity: O(1)