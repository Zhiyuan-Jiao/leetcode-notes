# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums = sorted(nums)
#         # Brute Force
#         # Time complexity: O(2^n)
#         # Space complexity: (n)
#         res = []
#         def dfs(cur, i):
#             print(cur)
#             # base case
#             if sum(cur) == target and len(cur) == 4:
#                 if Counter(cur) not in [Counter(j) for j in res.copy()]:
#                     res.append(cur.copy())
#                     return
#             if i >= len(nums) or len(cur) >= 4:
#                 return
            
#             cur.append(nums[i])
#             while i + 1 < len(nums) and nums[i] == nums[i + 1]:
#                 i += 1
#             dfs(cur, i + 1)
#             cur.pop()
#             dfs(cur, i + 1)
        
#         dfs([], 0)
#         return res

# Time complexity: O(n^3)
# Space complexity: O(1)
class Solution:
    def fourSum(self, nums, target):
        def findNsum(cur, N, l, target):
            if N != 2:
                for i in range(l, len(nums)):
                    if i > l and nums[i] == nums[i - 1]:
                        continue
                    cur.append(nums[i])
                    findNsum(cur, N - 1, i + 1, target - nums[i])
                    cur.pop()
                return
            else:
                r = len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] > target:
                        r -= 1
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        res.append(cur.copy() + [nums[l], nums[r]])
                        l, r = l + 1, r - 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

        nums.sort()
        res = []
        findNsum([], 4, 0, target)
        return res