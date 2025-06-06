class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def helper(a, b, order):
            for j in range(min(len(a), len(b))):
                if a[j] == b[j]: continue
                # print(a[j], order.index(a[j]), b[j], order.index(b[j]))
                return order.index(a[j]) < order.index(b[j])
            return len(a) <= len(b)
        
        for i in range(1, len(words)):
            cur, pre = words[i], words[i - 1]
            if not helper(pre, cur, order): return False
        return True