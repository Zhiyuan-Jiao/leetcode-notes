class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        res.append([1, 1])
        n = 2
        while n < numRows:
            newRow = [1] * (n + 1)
            for i in range(1, len(newRow) - 1):
                newRow[i] = res[n - 1][i - 1] + res[n - 1][i]
            res.append(newRow)
            n += 1
        return res
# T: O(n) S: O(n)