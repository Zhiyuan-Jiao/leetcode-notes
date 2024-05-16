class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # build the sticker letter count
        stickCount = []
        for i, s in enumerate(stickers):
            stickCount.append({})
            for c in s:
                stickCount[i][c] = stickCount[i].get(c, 0) + 1
        
        dp = {} # subseq of target -> min num of sticks
        def dfs(t, stick):
            if t in dp:
                return dp[t]
            
            res = 1 if stick else 0
            remainT = ""
            for c in t:
                if c in stick and stick[c] > 0:
                    stick[c] -= 1
                else:
                    remainT += c
            if remainT:
                used = float("inf")
                for s in stickCount:
                    if remainT[0] not in s:
                        continue
                    used = min(used, dfs(remainT, s.copy()))
                dp[remainT] = used
                res += used
            return res
        
        res = dfs(target, {})
        return res if res != float("inf") else -1

        # Time complexity: O(m*n + 2^n)
        # Space complexity: O(m*n)