import heapq, collections
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        minHeap, maxHeap, removedDict = [], [], collections.defaultdict(int)

        # 1. add initial window
        for i in range(k):
            heapq.heappush(maxHeap, -nums[i])
        for j in range(k // 2):
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))
        
        res = []
        median = -maxHeap[0] if k % 2 else (-maxHeap[0] + minHeap[0]) / 2.0
        res.append(median)
        balance = 0

        # 2. slide the window
        for idx in range(k, len(nums)):
            prev = nums[idx - k]
            removedDict[prev] += 1

            # use pivot (current max of lower half) instead of median
            pivot = -maxHeap[0]

            if prev <= pivot:
                balance -= 1
            else:
                balance += 1

            nxt = nums[idx]
            if nxt <= pivot:
                heapq.heappush(maxHeap, -nxt)
                balance += 1
            else:
                heapq.heappush(minHeap, nxt)
                balance -= 1

            # rebalance: positive -> move max→min; negative -> move min→max
            if balance > 0:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))
                balance -= 2
            elif balance < 0:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))
                balance += 2

            # prune stale values from both heaps
            while maxHeap and removedDict[-maxHeap[0]] > 0:
                removedDict[-maxHeap[0]] -= 1
                heapq.heappop(maxHeap)
            while minHeap and removedDict[minHeap[0]] > 0:
                removedDict[minHeap[0]] -= 1
                heapq.heappop(minHeap)

            median = -maxHeap[0] if k % 2 else (-maxHeap[0] + minHeap[0]) / 2.0
            res.append(median)

        return res

# T: O(nlogk) S: O(k)