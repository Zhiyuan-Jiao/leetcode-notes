class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.minHeap = k, nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        

#Time complexity: O(n + (n-k)logn) / O(n) for initialize, O(logn) for add

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)







