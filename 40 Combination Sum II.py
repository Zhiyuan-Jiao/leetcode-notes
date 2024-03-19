class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates  = sorted(candidates)
        res = []
        def dfs(i, cur, total):
            # base case
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target: return
            
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]: i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

# Time complexity: O(nlogn + 2^n) = O(2^n)
# Space complexity: O(2^n)