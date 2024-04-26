class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry, i = 1, len(digits) - 1
        while carry > 0 and i >= 0:
            digits[i] += carry
            carry = 0
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
            i -= 1
        if i < 0 and carry == 1:
            res = []
            res.append(1)
            res.extend(digits)
            return res
        return digits

# Time complexity: O(n)
# Space complexity: O(n)