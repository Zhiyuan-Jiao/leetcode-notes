class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1 # use the ascii value to represent each character for the key
            res[tuple(count)].append(s) # dict key can only be immutables
        
        return res.values()

# Time complexity: O(m*n)
# Space complexity: O(n)