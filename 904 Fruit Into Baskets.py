class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2: return len(fruits)

        baskets = {}
        res = 2
        i = 0
        for j, f in enumerate(fruits):
            if len(baskets) < 2 or f in baskets:
                baskets[f] = baskets.get(f, 0) + 1
                continue

            print(baskets)
            res = max(res, sum(baskets.values()))
            while len(baskets) > 1:
                baskets[fruits[i]] -= 1
                if baskets[fruits[i]] == 0: baskets.pop(fruits[i])
                i += 1
            baskets[f] = 1
        res = max(res, j - i + 1)
        return res