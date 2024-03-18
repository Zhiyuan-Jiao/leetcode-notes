class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        def dfs(subset, i):
            # base case
            if i == len(nums): 
                if subset not in res:
                    res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(subset, i + 1)
            subset.pop()
            if i + 1 < len(nums) and nums[i] == nums[i + 1]: i += 1 # skip next value if it is a duplicate
            dfs(subset, i + 1)

        
        dfs([], 0)
        return res

# Time complexity: O(n2^n)
# Space complexity: O(n)