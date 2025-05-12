class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        words = ['leet', 'code', 'question', 'code']
        k = 2

        res = ['code', 'leet']
        '''

        heap = []
        count = Counter(words)
        for s in count:
            heapq.heappush(heap, Pair(s, count[s]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [p.word for p in sorted(heap, reverse=True)]