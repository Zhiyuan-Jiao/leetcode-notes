class StockSpanner:

    def __init__(self):
        self.prices = [float("inf")]
        self.stack = [0] # mono decreasing stack

    def next(self, price: int) -> int:
        # print(self.stack)
        self.prices.append(price)

        if not self.stack:
            self.stack.append(len(self.prices) - 1)
            return 1

        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()
        self.stack.append(len(self.prices) - 1)
        return self.stack[-1] - self.stack[-2] if len(self.stack) > 1 else 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)