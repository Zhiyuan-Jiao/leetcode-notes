class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {} # (i, j) -> match or not at the specified index

        def dfs(i, j):
            # base case
            if i >= len(s) and j >= len(p):
                return True
            if i >= len(s):
                if j + 1 < len(p) and p[j + 1] == "*":
                    return dfs(i, j + 1)
                if p[j] == "*":
                    return dfs(i, j + 1)
                return False
            if j >= len(p):
                return False
            if (i, j) in dp:
                return dp[(i, j)]
            
            if s[i] == p[j] or p[j] == ".":
                if j + 1 < len(p) and p[j + 1] == "*": 
                    dp[(i, j)] = dfs(i + 1, j + 1) or dfs(i, j + 1)
                else:
                    dp[(i, j)] = dfs(i + 1, j + 1)
            elif p[j] == "*":
                if p[j - 1] == s[i] or p[j - 1] == ".":
                    dp[(i, j)] = dfs(i + 1, j + 1) or dfs(i + 1, j) or dfs(i, j + 1)
                else:
                    dp[(i, j)] = dfs(i, j + 1)
            elif j + 2 < len(p) and p[j + 1] == "*": 
                    dp[(i, j)] = dfs(i, j + 2)
            else:
                dp[(i, j)] = False
            return dp[(i, j)]
        
        return dfs(0, 0)

# Note: DP Bottom up
# Time complexity: O(m*n)
# Space complexity: O(m*n)