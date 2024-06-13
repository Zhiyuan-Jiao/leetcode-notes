class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        l = r = nums[0]
        res = []
        for n in nums:
            if n > r + 1: # out of range order
                # append previous interval to res
                if l == r:
                    res.append(str(l))
                else:
                    res.append(str(l) + "->" + str(r))
                # redefine l, r
                l = r = n
            else:
                r = n
        if l == r:
            res.append(str(l))
        else:
            res.append(str(l) + "->" + str(r))
        return res

# Time complexity: O(n)
# Space complexity: O(1)