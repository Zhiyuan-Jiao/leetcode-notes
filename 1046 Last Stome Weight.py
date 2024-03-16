class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x, y = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -(x - y))
        return -maxHeap[0]

# Time complexity: O(n + nlogn) = O(nlogn)
# Space complexity: O(n)