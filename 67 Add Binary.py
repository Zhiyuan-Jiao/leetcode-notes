class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        a, b = a[::-1], b[::-1]
        carry = 0

        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            total = digitA + digitB + carry
            char = total % 2
            res = str(char) + res
            carry = total // 2
        
        if carry: res = "1" + res
        return res

# Time complexity: O(n)
# Space complexity: O(1)