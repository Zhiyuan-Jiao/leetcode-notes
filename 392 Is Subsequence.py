class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Time complexity: O(2^n)
        # Space complexity: O(n)
        # def dfs(cur, i):
        #     # Base case
        #     if cur == s:
        #         return True
        #     if i >= len(t) or len(cur) > len(s):
        #         return False
            
        #     cur += t[i]
        #     if dfs(cur, i + 1): return True
        #     cur = cur[:-1]
        #     return dfs(cur, i + 1)
        
        # return dfs("", 0)

        # Time complexity: O(t)
        # Space complexity: O(1)
        if not s: return True
        if not t and s: return False
        curS, curT = 0, 0
        while curT < len(t):
            if s[curS] == t[curT]:
                curS += 1
                if curS == len(s): return True
            curT += 1
        return False
            