class Solution:
    def numSquares(self, n: int) -> int:
        dp = {} # n -> min perfect squares sum to n
        dp[0] = 0
        dp[1] = 1
        def dfs(n):
            # base case
            if not n:
                return 0
            
            if n in dp:
                return dp[n]
            
            dp[n] = float("inf")
            i = 1
            while i ** 2 <= n:
                dp[n] = min(dp[n], 1 + dfs(n - i ** 2))
                i += 1
            return dp[n]
        dfs(n)
        return dp[n]
# T: O(n * square root of n) S: O(n)

        # dp=[0]*(n+1)
        # for i in range(1,n+1):
        #     dp[i]=i
        #     for j in range(1,int(math.sqrt(i))+1):
        #         dp[i]=min(dp[i],dp[i-j*j]+1)
        # return dp[n]