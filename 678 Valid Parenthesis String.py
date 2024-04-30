class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            if c == ")":
                leftMin -= 1
                leftMax -= 1
            if c == "*":
                leftMin -= 1
                leftMax += 1
            if leftMin < 0:
                leftMin = 0
            if leftMax < 0:
                return False
        return 0 in range(leftMin, leftMax + 1)

# Note: Greedy, use two variable leftMin and leftMax which represent the range of our final result to track cases when we face a "*"
# Time complexity: O(n)
# Space complexity: O(1)