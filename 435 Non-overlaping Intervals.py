class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res

# Note: keep track of the merged end, if there is an overlap, keep the smaller end,
# smaller end will make sure it is the minimum number of intervals to remove.

# Time complexity: O(n)
# Space complexity: O(1)