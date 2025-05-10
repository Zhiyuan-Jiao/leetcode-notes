class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # find the possible matching values, if no value found return -1
        candidates = [tops[0], bottoms[0]]
        for i in range(1, len(tops)):
            for c in candidates.copy():
                if c not in [tops[i], bottoms[i]]:
                    candidates.remove(c)
                    if not candidates: return -1
        # print(candidates)
        res = float("inf")
        for c in candidates:
            res = min(res, len(tops) - tops.count(c), len(bottoms) - bottoms.count(c))
        return res