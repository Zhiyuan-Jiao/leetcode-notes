class DetectSquares:

    def __init__(self):
        self.points = {} # (x, y) -> frequency

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] = self.points.get((point[0], point[1]), 0) + 1

    def count(self, point: List[int]) -> int:
        res = 0
        for x, y in self.points:
            if x != point[0] and y != point[1] and abs(x - point[0]) == abs(y - point[1]):
                res += self.points.get((x, point[1]), 0) * self.points.get((point[0], y), 0) * self.points[(x, y)]
        return res

# Note: check diagonally to see if forming a square is possible

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)