class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-1 for i in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = collections.deque()

        while maxHeap or q:
            time += 1
            
            # there are tasks ready to be process
            if maxHeap: 
                count = 1 + heapq.heappop(maxHeap)
                if count: q.append(count)

            # there are tasks waiting to be processed and no wait time
            if q and q[0][1] == time: 
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

# Time complexity: O(n)
# Space complexity: O(n)