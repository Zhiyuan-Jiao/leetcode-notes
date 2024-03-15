n = 10
maxHeap = [-i for i in range(n)]
minHeap = [i for i in range(n)]
# time complexity: O(n)
heapq.heapify(maxHeap)
heapq.heapify(minHeap)

# time complexity: O(logn), n = 10
max = -heapq.heappop(maxHeap)
min = heapq.heappop(minHeap)

v = 10
# time complexity: O(logn), n = 10
heapq.heappush(maxHeap, -v)
heapq.heappush(minHeap, v)