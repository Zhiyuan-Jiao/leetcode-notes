class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float("inf")

        # 1. sort nlogn
        nums.sort()

        # 2. two pointer
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]: continue

            nt = target - n
            l, r = i + 1, len(nums) - 1
            while l < r:
                curS = nums[l] + nums[r]
                if curS > nt:
                    r -= 1
                    if abs(target - res) > abs(curS + n - target):
                        res = curS + n
                elif curS < nt:
                    l += 1
                    if abs(target - res) > abs(curS + n - target):
                        res = curS + n
                else:
                    res = target
                    return res
        
        # edge case 1: duplicate number
        return res

# T: O(nlogn + n^2) S: O(1)