class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if target in triplets: return True

        good = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3

# Note: if a triple has value larger than target, we can skip it. All the remain value will be
# equal to or smaller than target so as long as the target value is in there, it is garanteed that
# there will be a solution

# Time complexity: O(n)
# Space complexity: O(1)