class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_result = start ^ goal
        res = 0
        while xor_result:
            res += xor_result & 1
            xor_result >>= 1
        return res