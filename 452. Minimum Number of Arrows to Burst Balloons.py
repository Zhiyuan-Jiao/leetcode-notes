class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 1
        points = sorted(points)
        curInterval = points[0]
        for l, r in points[1:]:
            if curInterval[1] < l:
                curInterval = [l, r]
                res += 1
            else:
                curInterval = [max(curInterval[0], l), min(curInterval[1], r)]
        return res

# T: O(n), S: O(1)