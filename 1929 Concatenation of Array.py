class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # l, r = 0, len(nums)
        # res = [0] * (len(nums) * 2)
        # while r < len(res):
        #     res[l], res[r] = nums[l], nums[l]
        #     l += 1
        #     r += 1
        # return res

        res = []
        for i in range(2):
            for n in nums:
                res.append(n)
        return res

# Time complexity: O(n)
# Space complexity: O(n)