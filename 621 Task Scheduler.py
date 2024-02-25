class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Create the max heap and q
        count = Counter(tasks)
        maxHeap = [-i for i in count.values()]
        heapq.heapify(maxHeap)
        q = collections.deque()

        time = 0
        # as long as there are tasks waiting to be processed
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time