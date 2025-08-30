class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []              # use a list to collect digits
        carryOver = 0
        p1, p2 = len(num1) - 1, len(num2) - 1

        while p1 >= 0 or p2 >= 0 or carryOver:
            cur = carryOver
            if p1 >= 0:
                cur += int(num1[p1])
                p1 -= 1
            if p2 >= 0:
                cur += int(num2[p2])
                p2 -= 1

            res.append(str(cur % 10))   # append digit (in reverse order)
            carryOver = cur // 10

        res.reverse()                   # in-place reversal, O(1) extra
        return ''.join(res)

# T: O(max(m, n)) S: O(1)
