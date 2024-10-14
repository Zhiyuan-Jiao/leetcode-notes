class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([j[1] for j in intervals])
        s, e = 0, 0
        res, count = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res

# T: O(nlogn + n) = O(nlogn)
# S: O(N)
# Note: Separate and sort start and end time in two list, count max room