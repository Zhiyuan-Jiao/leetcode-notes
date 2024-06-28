class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        c1 = c2 = 0
        res = ""
        while c1 < len(word1) and c2 < len(word2):
            res += word1[c1]
            res += word2[c2]
            c1 += 1
            c2 += 1
        if c1 < len(word1): res += word1[c1:]
        if c2 < len(word2): res += word2[c2:]
        return res
    
# T: O(min(m, n)), S: O(1) 