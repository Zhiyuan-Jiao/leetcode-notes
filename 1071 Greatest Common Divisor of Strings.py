class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        str1 = "ABABABAB"
        str2 = "ABAB"
        '''
        # candidates = []
        # # tranverse to get the all possible substrs that str1[:i] == str2[:i] O(min(n, m))
        # for i in range(min(len(str1), len(str2))):
        #     if str1[i] != str2[i]: break
        #     candidates.append(str1[:i + 1])
        # if not candidates: return ""
        
        # def canDivide(candidate, string): # O(n)
        #     l, r = 0, len(candidate) - 1
        #     while l <= r < len(string) and string[l:r + 1] == candidate:
        #         # print(l, r)
        #         l, r = r + 1, r + len(candidate)
        #     return l == len(string)

        # # print(canDivide("A", "AA"))

        # # try and see if each candidates can actually divide both str1 and str2 O(mlogm + m ^ 2)
        # candidates.sort(reverse=True)
        # for c in candidates:
        #     if canDivide(c, str1) and canDivide(c, str2):
        #         return c
        # return ""

        return str1[:gcd(len(str1), len(str2))] if str1 + str2 == str2 + str1 else ""