class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, comp):
            nonlocal res

            # base case
            if len(comp) == k:
                res.append(comp.copy())
                return
            
            for i in range(start, n + 1):
                comp.append(i)
                start += 1
                backtrack(start, comp)
                comp.pop()
            
        backtrack(1, [])
        return res

# Time: O(n^k), Space: O(k)
# Note: Use index to track numbers used befor to eliminate duplicate, 1 -> 2, 3, 4 ..... 2 -> 3, 4 ..... 3 -> 4