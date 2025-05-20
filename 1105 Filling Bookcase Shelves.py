class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # dp = {}  # (idx, widthRemaining, curMaxHeight) -> min height to finish the rest 
        # def dfs(i, width, maxH):
        #     # base case
        #     if i == len(books):
        #         return maxH
        #     if (i, width, maxH) in dp:
        #         return dp[(i, width, maxH)]

        #     if width >= books[i][0]:
        #         addToCur = dfs(i + 1, width - books[i][0], max(maxH, books[i][1]))
        #     else:
        #         addToCur = float("inf")
        #     addToNext = dfs(i + 1, shelfWidth - books[i][0], books[i][1]) + maxH
        #     res = min(addToCur, addToNext)
        #     dp[(i, width, maxH)] = res
        #     return res
        # return dfs(0, shelfWidth, 0)

        dp = {}
        def dfs(i):
            if i == len(books):
                return 0
            if i in dp:
                return dp[i]
            
            cur_height = 0
            cur_width = 0
            res = float("inf")
            for j in range(i, len(books)):
                if cur_width + books[j][0] > shelfWidth:
                    break
                cur_height = max(cur_height, books[j][1])
                cur_width += books[j][0]
                res = min(res, dfs(j + 1) + cur_height)
            dp[i] = res
            return res
        return dfs(0)