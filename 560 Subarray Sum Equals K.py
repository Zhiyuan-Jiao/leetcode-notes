class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Brute Force: Time complexity: O(n^2)
        # res = 0
        # for l in range(len(nums)):
        #     curSum = 0
        #     for r in range(l, len(nums)):
        #         curSum += nums[r]
        #         if curSum == k:
        #             res += 1
        # return res

        res = 0
        prefixSum = 0
        prefixSums = {}
        prefixSums[0] = 1
        for i in range(len(nums)):
            prefixSum += nums[i]
            res += prefixSums.get(prefixSum - k, 0) # check if a prefixsum with different k exist in hashmap
            prefixSums[prefixSum] = prefixSums.get(prefixSum, 0) + 1
        
        return res

        # time complexity: O(n)
        # Space complexity: O(n)