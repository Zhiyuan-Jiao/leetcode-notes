class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        good_pair = 0
        for i, n in enumerate(nums):
            key = n - i
            good_pair += freq[key]
            freq[key] += 1
        return len(nums) * (len(nums) - 1) // 2 - good_pair