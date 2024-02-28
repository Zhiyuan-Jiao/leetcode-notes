class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

# [100, 4, 200, 1, 3, 2]
# the previous of each start of a sequence must not present in the array
# ? <- 1, 2, 3, 4 ...... ? <- 100 .... ? <- 200

        if not nums: return 0

        nSet = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in nSet: # start of a sequence
                length = 1
                while n + length in nSet: 
                    length += 1
                res = max(res, length)
        return res

# Time complexity: O(n)
# Space complexity: O(n)