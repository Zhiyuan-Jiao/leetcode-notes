class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.sentences = defaultdict(int)

class Pair:
    def __init__(self, freq, sentence):
        self.freq = freq
        self.sentence = sentence
    
    def __lt__(self, other):
        return self.sentence > other.sentence if self.freq == other.freq else self.freq < other.freq

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.cur = self.root
        self.curS = ""
        self.dead = TrieNode()
        # build the trie
        for s, t in zip(sentences, times):
            node = self.root
            for c in s:
                node = node.children[c]
                node.sentences[s] = t

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.addToTrie(self.curS)
            self.cur = self.root
            self.curS = ""
            return []

        self.curS += c

        if c not in self.cur.children:
            self.cur = self.dead
            return []

        self.cur = self.cur.children[c]
        # print(self.cur.sentences)
        h = []
        for s, f in self.cur.sentences.items():
            heappush(h, Pair(f, s))
            if len(h) > 3:
                heappop(h)
        return [heappop(h).sentence for i in range(len(h))][::-1]
    
    def addToTrie(self, s):
        cur = self.root
        for c in s:
            cur = cur.children[c]
            cur.sentences[s] += 1
        

# Usage example:
# obj = AutocompleteSystem(["i love you","island","ironman","i love leetcode"], [5,3,2,2])
# print(obj.input('i'))   # ["i love you","i love leetcode","island"]
# print(obj.input(' '))   # ["i love you","i love leetcode"]
# print(obj.input('a'))   # []
# print(obj.input('#'))   # []
