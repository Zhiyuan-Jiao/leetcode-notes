class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

# maxHeap

        cnt = Counter(nums)
        maxHeap = []
        for i in cnt:
            heapq.heappush(maxHeap, (cnt[i] * -1, i)) # use a tuple to store values, key pair into heap, heap will be able to sort based on the first value in tuple
        res = []
        for j in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res

# Time complexity: O(klogn)
# Space complexity: O(k)

# bucket sort (use frequency as index)
# nums = [1, 1, 2, 2, 3]
# frequency: 0   1   2   3   4   5   6
# num:      [ ] [3] [2] [1] [ ] [ ] [ ] 

        cnt = Counter(nums)
        bkt = [[] for i in range(len(nums) + 1)]
        for n, c in cnt.items():
            bkt[c].append(n)
        res = []
        for i in range(len(bkt) - 1, 0, -1):
            for n in bkt[i]:
                res.append(n)
                if len(res) == k:
                    return res

# Time compleixty: O(n)
# Space complexity: O(n)