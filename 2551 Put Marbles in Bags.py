class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1: return 0
        # minS, maxS = float("inf"), float("-inf")
        # def dfs(i, cuts):
        #     nonlocal minS, maxS
        #     # base case
        #     if len(cuts) == k - 1:
        #         curS = 0
        #         for j, c in enumerate(cuts):
        #             if j == 0:
        #                 curS += weights[0] + weights[cuts[j]]
        #             else:
        #                 curS += weights[cuts[j - 1] + 1] + weights[cuts[j]]
        #         # print(cuts)
        #         curS += weights[cuts[-1] + 1] + weights[-1]
        #         minS, maxS = min(minS, curS), max(maxS, curS)
        #         return
        #     if i == len(weights) - 1:
        #         return
            
        #     cuts.append(i)
        #     dfs(i + 1, cuts)
        #     cuts.pop()
        #     dfs(i + 1, cuts)
        # dfs(0, [])
        # # print(minS, maxS)
        # return maxS - minS

        splits = [weights[i - 1] + weights[i] for i in range(1, len(weights))]
        splits = sorted(splits)
        maxS = sum(splits[-(k - 1):])
        minS = sum(splits[:k - 1])
        return maxS - minS

# Note: only cares about splits in the middle 