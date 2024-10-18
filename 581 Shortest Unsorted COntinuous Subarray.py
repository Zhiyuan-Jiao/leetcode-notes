class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # start, end = -1, -1
        # for i, n in enumerate(nums[:-1]):
        #     minLeft = min(nums[i + 1:])
        #     if n > minLeft:
        #         if start == -1:
        #             start = i
        #         for j in range(i + 1, len(nums)):
        #             if nums[j] < n:
        #                 end = max(end, j)
        #         if end == len(nums) - 1:
        #             break
        # return end - start + 1 if start != -1 else 0

# T: O(n*n) S: O(1)

        sortedNums = sorted(nums)
        l, r = 0, len(nums) - 1
        res = [-1, -1]
        while r >= 0 and l < len(nums):
            if res[0] == -1 and nums[l] != sortedNums[l]:
                res[0] = l
            if res[1] == -1 and nums[r] != sortedNums[r]:
                res[1] = r
            if res[0] != -1 and res[1] != -1:
                return res[1] - res[0] + 1
            print(res)
            l += 1
            r -= 1
        return 0

# T: O(nlogn) S: O(n)