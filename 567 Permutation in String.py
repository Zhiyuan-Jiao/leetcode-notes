class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        match = 0
        for i in range(26):
            match += 1 if s1Count[i] == s2Count[i] else 0
        if match == 26: return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            right = ord(s2[r]) - ord("a")
            s2Count[right] += 1
            if s1Count[right] == s2Count[right]:
                match += 1
            elif s1Count[right] + 1 == s2Count[right]:
                match -= 1

            left = ord(s2[l]) - ord("a")
            s2Count[left] -= 1
            if s1Count[left] == s2Count[left]:
                match += 1
            elif s1Count[left] - 1 == s2Count[left]:
                match -= 1
            l += 1

            if match == 26: return True

# Time complexity: O(n)
# Space complexity: O(26 * 2) = O(1)