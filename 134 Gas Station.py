class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                start = i + 1
                total = 0
        return start

# Note: Greedy
# [ 1,  2,  3, 4, 5]
# [ 3,  4,  5, 1, 2]
# [-2, -2, -2, 3, 3]
#   x   x   x  ^

# Time complexity: O(n)
# Space complexity: O(1)