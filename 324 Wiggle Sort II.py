class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sortedNums = sorted(nums)
        l, r = len(sortedNums) // 2 if len(sortedNums) % 2 else len(sortedNums) // 2 - 1, len(sortedNums) - 1
        for i in range(0, len(nums) - 1, 2):
            print(i)
            nums[i], nums[i + 1] = sortedNums[l], sortedNums[r]
            l -= 1
            r -= 1
        if len(sortedNums) % 2:
            nums[-1] = sortedNums[0]

# T: O(nlogn) S: O(n)
