class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            left >>= 1
            right >>= 1
            i += 1
        return left << i

# T: O(logn) S: O(1)
# Note: by chopping off from the right, eliminate possible zeros