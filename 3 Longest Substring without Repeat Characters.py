class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashTable = set()
        maxLen = 0
        left = 0
        
        for right in range(len(s)):
            while s[right] in hashTable:
                hashTable.remove(s[left])
                left += 1
            hashTable.add(s[right])
            maxLen = max(maxLen, len(hashTable))
        
        return maxLen


# Algorithm: Sliding window: keeps moving left until there is no duplicate in the set, then move right
# Time complexity: O(n)
# Space complexity: O(n)