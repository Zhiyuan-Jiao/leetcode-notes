class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.sum = 0
        self.q = collections.deque()
        

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.sum -= self.q.popleft()
        self.q.append(val)
        self.sum += val
        return self.sum / len(self.q)

    # Time complexity: O(1)
    # Space complexity: O(n)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)