class Solution:
    def numberOfWays(self, s: str) -> int:
        '''
        001101


        '''
        res = 0
        one = zero = zero_one = one_zero = 0
        for c in s:
            if c == "0":
                res += zero_one
                one_zero += one
                zero += 1
            else:
                res += one_zero
                zero_one += zero
                one += 1
        return res