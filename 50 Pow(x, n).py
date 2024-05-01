class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if not n: return 1

        # k = abs(n)
        # res = x
        # while k > 1:
        #     k -= 1
        #     res *= x
        # return 1 / res if n < 0 else res

        def helper(x, n):
            # base case
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x, n // 2)
            res = res * res
            return x * res if n % 2 else res
            
        
        res = helper(x, abs(n))
        return 1 / res if n < 0 else res

# Note: Divide and conquer, 2^10 = 2^5 * 2^5 = 2 * 2^2 * 2^2 ....
# Time complexity: O(logn)
# Space complexity: O(logn)