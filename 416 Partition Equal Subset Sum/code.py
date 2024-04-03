class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1: return False

        # def dfs(cur, i):
        #     # base case
        #     if sum(cur) > sum(nums) / 2 or i == len(nums): return False

        #     if sum(cur) == sum(nums) / 2: return True

        #     cur.append(nums[i])
        #     if dfs(cur, i + 1): return True
        #     cur.pop()
        #     return dfs(cur, i + 1)

        # return dfs([], 0)


        dpSet = set([0])
        for num in nums:
            newSet = dpSet.copy()
            for dpN in dpSet:
                newSet.add(dpN + num)
                dpSet = newSet
        return sum(nums) / 2 in dpSet

# Time complexity: O(n * sumN)
# Space complexity: O(sumN)
            