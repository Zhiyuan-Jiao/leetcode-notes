class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1] and res[j] <= res[j + 1]:
                res[j] = res[j + 1] + 1
        print(res)
        return sum(res)

# T: O(n) S: O(n)
# Note: loop through ratings twice forward and backward, increase the candy when rating is higher than the last one.