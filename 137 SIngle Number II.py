class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize seen_once and seen_twice to 0
        seen_once = seen_twice = 0

        # Iterate through nums
        for num in nums:
            # Update using derived equations
            seen_once = (seen_once ^ num) & (~seen_twice)
            seen_twice = (seen_twice ^ num) & (~seen_once)

        # Return integer which appears exactly once
        return seen_once

# a) seen_once = (seen_once ^ num) & (~seen_twice)
# seen_once ^ num: The XOR operation will toggle bits in seen_once based on num. If a bit is 1 in num and not in seen_once, it becomes 1 in seen_once. If it's already 1 in seen_once, XOR flips it back to 0. So, it tracks bits that have appeared exactly once so far.
# & (~seen_twice): This ensures that bits that have already appeared twice (tracked by seen_twice) do not get set in seen_once. It essentially "removes" bits from seen_once if they have already appeared twice.

# b) seen_twice = (seen_twice ^ num) & (~seen_once)
# seen_twice ^ num: Similar to the previous line, this XOR toggles bits in seen_twice based on num. It adds bits that have been seen twice and removes them if seen the third time.
# & (~seen_once): This ensures that bits that have been added to seen_once (i.e., those that are being tracked as "seen once") are not counted again in seen_twice.