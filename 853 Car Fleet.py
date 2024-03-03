class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1: return 1

        cars = sorted(zip(position, speed))
        stack = []

        for p, s in cars[::-1]:
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

# note: compare the finish time between cars, if a car with longer distance finished before a car with
#       shorter distance, it will difinitely merged into the slower car fleet.

# Time complexity: O(n)
# Space complexity: O(n)