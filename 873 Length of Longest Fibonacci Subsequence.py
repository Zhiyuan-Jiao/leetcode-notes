class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        valMap = {n:i for i, n in enumerate(arr)}
        dp = {} # (i, j) -> max fib subseq can form starting i, j

        res = 0
        for i in range(len(arr) - 3, -1, -1):
            for j in range(len(arr) - 2, i, -1):
                pre, cur = arr[i], arr[j]
                nxt = pre + cur
                if nxt not in valMap: continue
                dp[(i, j)] = dp.get((j, valMap[nxt]), 2) + 1
                res = max(res, dp[(i, j)])
        return res