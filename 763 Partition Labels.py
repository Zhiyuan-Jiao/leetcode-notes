class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rightmost = {c:i for i, c in enumerate(s)}
        right, left = 0, 0

        res = []
        for i, c in enumerate(s):
            right = max(right, rightmost[c])

            if i == right:
                res += [right - left + 1]
                left = i + 1

        return res

# Note: use two pointer l, r to track the start and end of the current interval,
# if we get a new character with higher end position, update the r pointer.

# Time complexity: O(n)
# Space complexity: O(c), c -> # of distinct characters in s