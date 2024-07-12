class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(s):
            total, part = 0, 1
            for n in nums:
                if total + n > s:
                    part += 1
                    if part > k:
                        return False
                    total = n
                else:
                    total += n
            return True
        
        l, r = max(nums), sum(nums)
        res = l
        while l <= r:
            m = l + (r - l) // 2
            if feasible(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

# Note: Use Binary Search to find the least possbile largest sum.
# Time complexity: O(nlogn) Space complexity: O(1)