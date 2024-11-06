class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        wordsMap = Counter(words)
        res = []
        for i in range(wordLen):
            l = r = i
            curMap = Counter()
            count = 0
            while r + wordLen <= len(s):
                curWord = s[r:r + wordLen]
                r += wordLen
                if curWord in wordsMap:
                    curMap[curWord] += 1
                    count += 1
                    while curMap[curWord] > wordsMap[curWord]:
                        curMap[s[l:l + wordLen]] -= 1
                        l += wordLen
                        count -= 1
                    if count == len(words):
                        res.append(l)
                else:
                    curMap.clear()
                    count = 0
                    l = r
        return res

# T: O(n) S: O(n)
# Note: use sliding window to check for each start index pattern in s