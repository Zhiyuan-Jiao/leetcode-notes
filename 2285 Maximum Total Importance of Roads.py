class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # count number of road each city connected to and sort based on it O(r + nlogn)
        roadMap = [0] * n
        for c1, c2 in roads:
            roadMap[c1] += 1
            roadMap[c2] += 1
        # assign the larger value to the city with greater number of roads O(n)
        res = 0
        i = 1
        for roads in sorted(roadMap):
            res += roads * i
            i += 1
        return res