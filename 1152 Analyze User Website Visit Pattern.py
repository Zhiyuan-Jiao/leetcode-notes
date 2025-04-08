class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = sorted(zip(timestamp, username, website))
        userMap = defaultdict(list)
        for t, u, w in visits:
            userMap[u].append(w)
        patternCounts = {}
        for webs in userMap.values():
            patterns = set(combinations(webs, 3))
            for pattern in patterns:
                patternCounts[pattern] = patternCounts.get(pattern, 0) + 1
        # print(patternCounts)
        maxPattern, maxScore = "", float("-inf")
        for pattern, count in patternCounts.items():
            if count > maxScore or (count == maxScore and pattern < maxPattern):
                maxPattern, maxScore = pattern, count
        return maxPattern
