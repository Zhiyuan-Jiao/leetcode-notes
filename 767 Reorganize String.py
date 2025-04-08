class Solution:
    def reorganizeString(self, s: str) -> str:
        cCount = Counter(s)
        pq = [[-cCount[c], c] for c in cCount]
        heapq.heapify(pq)
        
        res = ""
        while pq:
            cur = heapq.heappop(pq)[1]
            res += cur
            cCount[cur] -= 1
            if cCount[cur] == 0: cCount.pop(cur)
            if pq:
                next = heapq.heappop(pq)[1]
                res += next
                cCount[next] -= 1
                if cCount[next] == 0: cCount.pop(next)
                if cCount[cur]: heapq.heappush(pq, [-cCount[cur], cur])
                if cCount[next]: heapq.heappush(pq, [-cCount[next], next])
        print(res)
        return res if len(cCount) == 0 else ""