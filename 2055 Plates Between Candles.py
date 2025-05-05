class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        closestL, closestR = [], []
        curClosest = -1
        for i, n in enumerate(s):
            if n == "|":
                curClosest = i
            closestL.append(curClosest)
        curClosest = len(s)
        for j in range(len(s) - 1, -1, -1):
            if s[j] == "|":
                curClosest = j
            closestR.append(curClosest)
        closestR = closestR[::-1]
        # print(closestL)
        # print(closestR)
        validPlatesSum = 0
        lastCandle = -1
        validPlates = []
        for k, n in enumerate(s):
            if n == "|":
                if lastCandle != -1: validPlatesSum += k - lastCandle - 1
                lastCandle = k
            validPlates.append(validPlatesSum)
        # print(validPlates)
        res = []
        for q1, q2 in queries:
            if closestR[q1] > q2 or closestL[q2] < q1:
                res.append(0)
                continue
            res.append(validPlates[closestL[q2]] - validPlates[closestR[q1]])
        return res
