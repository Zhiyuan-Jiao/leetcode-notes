class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def helper(x, y):
            # base case
            if x == 0:
                return 0
            if y == 0:
                return 1
            
            res = helper(x, y // 2)
            res = res * res % (10**9 + 7)
            return x * res if y % 2 else res

        return helper(5, (n + 1) // 2) * helper(4, n // 2) % (10**9 + 7)