class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        nums = sorted(nums, key=cmp_to_key(compare))
        return "".join(nums) if nums[0] != "0" else "0"

# T: O(nlogn) S: O(n)
# Note: check which goes first between two number by concat them then compare