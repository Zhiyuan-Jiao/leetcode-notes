class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = []
        res = []
        for i, n in enumerate(nums1):
            heapq.heappush(pq, [n + nums2[0], i, 0])
        while k > 0:
            s, idx1, idx2 = heapq.heappop(pq)
            res.append([nums1[idx1], nums2[idx2]])
            k -= 1
            if idx2 < len(nums2) - 1:
                heapq.heappush(pq, [nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1])
        return res

# T: O(klogn1) S: O(n1 + k)
# Note: It starts by inserting the pair sums of each element from nums1 and the first element of nums2 into a priority queue. 
# Since both arrays are sorted, the pair sums will be in increasing order.
# By utilizing a priority queue, the smallest sum pair is always accessible at the top. 
# The code then pops the smallest pair from the priority queue and adds it to the result vector. 
# Next, it inserts the next pair, which consists of the same element from nums1 but the next element from nums2.