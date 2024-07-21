class Solution:
    def trailingZeroes(self, n: int) -> int:
        # res = n
        # while n > 1:
        #     n -= 1
        #     res *= n
        # ans = 0
        # while res > 0 and res % 10 == 0:
        #     ans += 1
        #     res = res // 10
        # return ans
        res = 0
        for i in range(5, n + 1, 5):
            cur = i
            while cur % 5 == 0:
                res += 1
                cur //= 5
        return res

# Note: calculate the number of 5s which makes up 0
# T: O(logn) S: O(1)