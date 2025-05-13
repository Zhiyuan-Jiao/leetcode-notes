class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''
        s = "favadfwerq"
        k = 3
        vowel letter: a, e, i, o, u
        '''
        res = 0
        l = r = 0
        cur = 1 if s[0] in "aeiou" else 0
        while r - l + 1 < k:
            r += 1
            if s[r] in "aeiou": cur += 1
        res = cur
        while l <= r < len(s) - 1:
            if s[l] in "aeiou": cur -= 1
            l += 1
            r += 1
            if s[r] in "aeiou": cur += 1
            res = max(res, cur)
        return res