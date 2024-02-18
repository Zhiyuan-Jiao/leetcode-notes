class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s: return 0
        sign = 1
        i = 0
        if s[i] == "-": 
            sign = -1
            i += 1
        elif s[i] == "+": 
            i += 1
        res = ""
        for c in s[i:]:
            if not c.isdigit(): break
            res += c
        if res == "": return 0
        res = sign * int(res)
        if res > 2**31 - 1: return (2**31 - 1)
        if res < -2**31: return -2**31
        return res

        