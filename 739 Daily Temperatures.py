class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1: return [0]

        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append([t, i])

        return res

# Note: use a monotonic decreasing stack to track temp that cannot be processed rght now
# Time complexity: O(n)
# Space complexity: O(n)

