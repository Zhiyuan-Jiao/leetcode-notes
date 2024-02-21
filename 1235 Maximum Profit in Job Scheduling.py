class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            # base case
            if i == len(intervals): return 0
            if i in cache: return cache[i]
            
            # dont add i
            res = dfs(i + 1)

            # add i
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            # ge the max profit from either add or not add 
            cache[i] = res = max(res, intervals[i][2] + dfs(j))
            return res
        
        return dfs(0)

# Alogrithm: backtracking dfs, binary search, cache
# Time complexity: O(nlogn)
# Space complexity: O(n)