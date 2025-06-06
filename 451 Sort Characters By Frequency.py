class Solution:
    def frequencySort(self, s: str) -> str:
        # cntMap = Counter(s) # O(n)
        # res = []
        # sortedC = sorted(cntMap.keys(), key=lambda x: cntMap[x], reverse=True) # O(nlogn)
        # for c in sortedC: # O(n)
        #     res.extend(cntMap[c] * [c])
        # return "".join(res)

        buckets = defaultdict(list)
        cntMap = Counter(s)
        for c in cntMap:
            buckets[cntMap[c] - 1].append(c)
        res = ""
        for i in range(len(s) - 1, -1, -1):
            if i in buckets:
                for c in buckets[i]:
                    res += c * (i + 1)
        return res