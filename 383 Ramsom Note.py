class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_table = dict()
        for _ in magazine:
            if _ in hash_table.keys():
                hash_table[_] += 1
            else:
                hash_table[_] = 1
        for i in ransomNote:
            if i in hash_table.keys() and hash_table[i] > 0:
                hash_table[i] -= 1
            else:
                return False
        return True

# Time complexity: O(n)
# Space complexity: O(n)