class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        def enough(distance):
            # count = 0
            # for i in range(len(nums) - 1):
            #     for j in range(i + 1, len(nums)):
            #         if abs(nums[i] - nums[j]) <= distance:
            #             count += 1
            # return count >= k
            count = 0
            slow, fast = 0, 0
            while slow < len(nums) or fast < len(nums):
                while fast < len(nums) and nums[fast] - nums[slow] <= distance:
                    fast += 1
                count += fast - slow - 1
                slow += 1
            return count >= k
            
        
        l, r = 0, max(nums) - min(nums)
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            if enough(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

# T: O(nlogn) S: O(1)