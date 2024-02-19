class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        patternDict = dict()
        if beginWord not in wordList: wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                if pattern not in patternDict: patternDict[pattern] = []
                patternDict[pattern].append(word)
        
        q = collections.deque([beginWord])
        visited = set([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nei in patternDict[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            res += 1
        return 0

# Algorithm: Form a pattern dict to store all the word to its pattern, do a bfs using the pattern to find neighbor words
# Time complexity: O(n*n*m)
# Space complexity: O(n)