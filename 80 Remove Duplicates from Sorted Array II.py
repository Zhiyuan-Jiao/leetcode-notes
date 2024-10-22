class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if len(nums) < 3: 
        #     return len(nums)
        
        # lastNum = nums[1]
        # freq = 1 if nums[1] != nums[0] else 2
        # i = 2
        # for n in nums[2:]:
        #     if n == lastNum:
        #         freq += 1
        #         if freq < 3:
        #             nums[i] = n
        #             i += 1
        #     else:
        #         lastNum = n
        #         freq = 1
        #         nums[i] = n
        #         i += 1
        # return i

# T: O(n) S: O(1)
# Note: two pointer

        index = 2
        for i in range(2, len(nums)):
            if nums[index - 2] != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index

# T: O(n) S: O(1)
# Note: two pointer