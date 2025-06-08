class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # extract key timestamp into a hashmap
        timeMap = defaultdict(int)
        for n, src, dst in trips:
            timeMap[src] += n
            timeMap[dst] -= n
        # loop through the sorted timestamp
        cur = 0
        for t in sorted(timeMap.keys()):
            cur += timeMap[t]
            if cur > capacity: return False
        return True