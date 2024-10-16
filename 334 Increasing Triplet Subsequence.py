class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = float("inf")
        for n in nums:
            if n <= i:
                i = n
            elif n <= j:
                j = n
            else:
                return True
        return False

# T: O(n) S: O(1)
# Note: Greedy