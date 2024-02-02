class MinStack:

    def __init__(self):
        self.mainStack, self.minStack = [], []

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if not self.minStack: self.minStack.append(val)
        elif val >= self.minStack[-1]: self.minStack.append(self.minStack[-1])
        else: self.minStack.append(val)

    def pop(self) -> None:
        self.mainStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Algorithm: create a minStack to track the min at each value in stack in case a value is removed we dont know what the min of the rest
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()