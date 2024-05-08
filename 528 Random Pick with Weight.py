class Solution:

    def __init__(self, w: List[int]):
        self.prefixSums = []
        prefixSum = 0
        for n in w:
            prefixSum += n
            self.prefixSums.append(prefixSum)
        

    def pickIndex(self) -> int:
        target = self.prefixSums[-1] * random.random()
        l, r = 0, len(self.prefixSums) - 1
        while l < r:
            m = (l + r) // 2
            if self.prefixSums[m] == target:
                return m
            elif self.prefixSums[m] > target:
                r = m
            else:
                l = m + 1
        return l
            

# Note: use prefixsum array to create the sample list, use binary search to find the random target
# Time complexity: O(logn)
# Space complexity: O(n)
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()