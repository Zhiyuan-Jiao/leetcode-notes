class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0
        for c in s:
            if c == "(":
                count += 1
                res.append(c)
            elif c == ")":
                if count > 0:
                    count -= 1
                    res.append(c)
            else:
                res.append(c)
        filtered = []
        for c in res[::-1]:
            if count > 0 and c == "(":
                count -= 1
            else:
                filtered.append(c)
        return "".join(filtered[::-1])

# loop through s first time to remove extra ")", then loop reversely to remove extra "(" base on count
# Note: it is always right to remvoe the last "(" when there are extra "("
# Time complexity: O(n)
# Space complexity: O(n)