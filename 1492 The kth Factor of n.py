class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # for i in range(1, n + 1):
        #     if n % i == 0:
        #         k -= 1
        #         if k == 0:
        #             return i
        # return -1

        factors = []
        for i in range(1, int(sqrt(n)) + 1):
            if not n % i:
                factors.append([i, n // i])
                if len(factors) == k:
                    return i
        print(factors)
        if sqrt(n).is_integer():
            return factors[-(k - len(factors)) - 1][1] if len(factors) * 2 > k else -1
        return factors[-(k - len(factors))][1] if len(factors) * 2 >= k else -1


