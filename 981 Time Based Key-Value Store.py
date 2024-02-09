class TimeMap:

    def __init__(self):
        self.store = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store.keys():
            self.store[key] = []
        self.store[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store.keys(): return ""

        res = ""

        l, r = 0, len(self.store[key]) - 1
        while l <= r:
            m = (l + r) // 2
            if self.store[key][m][1] == timestamp: return self.store[key][m][0]
            elif self.store[key][m][1] > timestamp: r = m - 1
            else:
                res = self.store[key][m][0]
                l = m + 1
                
        return res
    
# Algorithm: Binary search: when m < timestamp, it mean m is a possible solution
# Time complexity: O(logn)
# Space complexity: O(n)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)