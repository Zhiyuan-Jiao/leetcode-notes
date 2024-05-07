class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(abbr) and j < len(word):
            if abbr[i].isnumeric():
                if abbr[i] == "0": return False
                abbrLen = 0
                while i < len(abbr) and abbr[i].isnumeric():
                    abbrLen = abbrLen * 10 + int(abbr[i])
                    i += 1
                j += abbrLen
            else:
                if abbr[i] != word[j]: 
                    return False
                else:
                    i += 1
                    j += 1
        return True if i == len(abbr) and j == len(word) else False

# Note: Two pointer
# Time complexity: O(n)
# Space complexity: O(1)