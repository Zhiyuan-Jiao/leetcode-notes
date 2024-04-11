class Solution:
    def getSum(self, a: int, b: int) -> int:
        bitShort = 0xffffffff  # used as a mask to ensure that the result within a 32-bit integer

        while b & bitShort != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return a & bitShort if b != 0 else a

# Note: use "& 0xffffffff" to prevent overflow caused by negative number in python