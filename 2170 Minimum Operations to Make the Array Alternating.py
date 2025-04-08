class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        max1 = Counter(nums[::2]).most_common(2) + [(0, 0)]
        max2 = Counter(nums[1::2]).most_common(2) + [(0, 0)]
        
        if max1[0][0] != max2[0][0]:
            return len(nums) - max1[0][1] - max2[0][1]
        
        return min(len(nums) - max1[0][1] - max2[1][1], len(nums) - max1[1][1] - max2[0][1])

