class MyQueue:

    def __init__(self):
        self.l1 = []
        

    def push(self, x: int) -> None:
        if not self.l1:
            self.l1.append(x)
        else:
            l2 = []
            for i in range(len(self.l1)):
                l2.append(self.l1.pop())
            self.l1.append(x)
            for j in range(len(l2)):
                self.l1.append(l2.pop())
        

    def pop(self) -> int:
        return self.l1.pop()
        

    def peek(self) -> int:
        return self.l1[len(self.l1) - 1]
        

    def empty(self) -> bool:
        return not self.l1
        


# Note: Use two stacks for the push operation