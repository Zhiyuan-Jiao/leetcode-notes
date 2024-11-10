class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # O(n^2)
        # for i in range(len(s)):
        #     for j in range(i + 1, len(s)):
        #         if s[i] == s[j] and t[i] != t[j] or t[i] == t[j] and s[i] != s[j]:
        #             return False
        # return True
    
        # O(n)
        # sc, tc = defaultdict(list), defaultdict(list)
        # for i in range(len(s)):
        #     sc[s[i]].append(i)
        #     tc[t[i]].append(i)
        # for j in sc.values():
        #     if j not in tc.values(): return False
        # return True
    
        cMap = dict()
        used = set()
        for i in range(len(s)):
            if s[i] in cMap:
                if cMap[s[i]] != t[i]: return False
            else:
                if t[i] in used: return False
                cMap[s[i]] = t[i]
                used.add(t[i])
        return True