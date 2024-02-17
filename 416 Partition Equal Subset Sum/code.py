class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums: return False
        target = sum(nums) / 2
        sumSet = set()
        sumSet.add(0)
        for i in nums:
            ns = []
            for s in sumSet:
                if i + s == target: return True
                ns.append(i + s)
            for s in ns:
                sumSet.add(s)
        return False
            