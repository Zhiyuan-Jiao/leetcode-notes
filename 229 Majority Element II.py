class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # nums = sorted(nums)
        # count = 0
        # res = []
        # for i, n in enumerate(nums):
        #     if i > 0 and n != nums[i - 1]:
        #         if count > len(nums) / 3:
        #             res.append(nums[i - 1])
        #         count = 0
        #     count += 1
        # if count > len(nums) / 3:
        #     res.append(nums[-1])
        # return res

# T: O(nlogn) S: O(1)

        majority1, majority2 = [0, 0], [0, 0]
        for n in nums:
            if majority1 and n == majority1[0]:
                majority1[1] += 1
            elif majority2  and n == majority2[0]:
                majority2[1] += 1
            elif not majority1 or majority1[1] == 0:
                majority1 = [n, 1]
            elif not majority2 or majority2[1] == 0:
                majority2 = [n, 1]
            else:
                majority1[1] -= 1
                majority2[1] -= 1
            
        res = []
        majority1[1], majority2[1] = 0, 0
        for n in nums:
            if n == majority1[0]:
                majority1[1] += 1
            elif n == majority2[0]:
                majority2[1] += 1
        
        if majority1[1] > len(nums) // 3:
            res.append(majority1[0])
        if majority2[1] > len(nums) // 3:
            res.append(majority2[0])
        return res

# Note: Since we are trying to find all elements that appear more than n/3 times
# the most amount element we could return is 2. We just need to find top 2 frequent element