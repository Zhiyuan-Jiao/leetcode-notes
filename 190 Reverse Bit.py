class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n % 2
            n = n >> 1
            res = res << 1
            res += bit
        return res

# Time complexity: O(32) -> O(1)
# Space complexity: O(1)