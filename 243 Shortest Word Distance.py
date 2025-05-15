class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = float("inf")
        i = j = -1
        for k, w in enumerate(wordsDict):
            # print(w, i, j)
            if w == word1:
                i = k
                if j != -1: res = min(res, i - j)
            elif w == word2:
                j = k
                if i != -1: res = min(res, j - i)
        return res