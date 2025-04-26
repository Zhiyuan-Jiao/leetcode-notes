class MaxStack:

    def __init__(self):
        self.stack = []
        self.pq = []
        self.next_idx = 0
        self.soft_delete = set()

    def push(self, x: int) -> None:
        new = (-x, self.next_idx)
        self.stack.append(new)
        heapq.heappush(self.pq, new)
        self.next_idx -= 1
    
    def clean(self):
        while self.stack and self.stack[-1] in self.soft_delete:
            self.stack.pop()
        while self.pq and self.pq[0] in self.soft_delete:
            heapq.heappop(self.pq)

    def pop(self) -> int:
        res = self.stack.pop()
        self.soft_delete.add(res)
        self.clean()
        return -res[0]

    def top(self) -> int:
        return -self.stack[-1][0]

    def peekMax(self) -> int:
        return -self.pq[0][0]

    def popMax(self) -> int:
        res = heapq.heappop(self.pq)
        self.soft_delete.add(res)
        self.clean()
        return -res[0]



# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()