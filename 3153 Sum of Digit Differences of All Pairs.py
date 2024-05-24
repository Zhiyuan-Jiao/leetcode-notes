class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        digitIdx = [{} for i in range(len(str(nums[0])))]
        for n in nums:
            n = str(n)
            for i, c in enumerate(n):
                digitIdx[i][int(c)] = digitIdx[i].get(int(c), 0) + 1
        print(digitIdx)
        res = 0
        for dIdx in digitIdx:
            for digit1 in range(10):
                for digit2 in range(10):
                    if digit1 not in dIdx or digit2 not in dIdx or digit1 == digit2: continue
                    res += dIdx[digit1] * dIdx[digit2]
        return res // 2

# T: O(nm) S: O(m*n)