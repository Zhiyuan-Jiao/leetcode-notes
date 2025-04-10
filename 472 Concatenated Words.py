class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        availableWs = set(words)

        dp = {} # sub words -> True/False
        def isConcat(w):
            if w in dp:
                return dp[w]
            res = False
            for i in range(len(w)):  # Start from 1 to ensure non-empty prefix
                subW = w[:i + 1]
                if subW in availableWs and (w[i + 1:] in availableWs or isConcat(w[i + 1:])):
                    res = True
            dp[w] = res
            return dp[w]
        

        # print(isConcat("catsdogcats", ["cat","cats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))

        res = []
        for w in words:
            availableWs.remove(w)
            if isConcat(w):
                res.append(w)
            availableWs.add(w)
        return res