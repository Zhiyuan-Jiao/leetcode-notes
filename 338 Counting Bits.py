class Solution:
    def countBits(self, n: int) -> List[int]:
        # res = []
        # for i in range(n + 1):
        #     res.append(0)
        #     while i:
        #         res[-1] += i % 2
        #         i = i >> 1 # or i = i // 2 also works
        # return res

# Time complexity: O(nlogn)

        res = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if i == offset * 2: offset = i
            res[i] = 1 + res[i - offset]
        return res
# Time complexity: O(n)