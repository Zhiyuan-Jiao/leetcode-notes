class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastPos = {c : i for i, c in enumerate(s)}
        seen = set()
        res = []
        for i, c in enumerate(s):
            if c in seen: continue
            while res and res[-1] > c and lastPos[res[-1]] > i:
                seen.remove(res.pop())
            res.append(c)
            seen.add(c)
        return "".join(res)

# T: O(n) S: O(26) = O(1)
# Note: keep track of the last position an character was seen, 
#       if a new smaller c found and there are more of the before charater, pop it from res