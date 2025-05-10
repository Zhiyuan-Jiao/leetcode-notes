class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3: return n
        f, p = [0] * (n + 1), [0] * (n + 1)
        f[1], f[2] = 1, 2
        p[2] = 1
        for i in range(3, n + 1):
            f[i] = (f[i - 1] + f[i - 2] + p[i - 1] * 2) % (10**9 + 7)
            p[i] = (p[i - 1] + f[i - 2]) % (10**9 + 7)
        return f[n]

# notes: Create two arrays, f and p, of size n+1, where f(k) represents the number of ways to fully cover a board of width k and p(k) represents the number of ways to partially cover a board of width k