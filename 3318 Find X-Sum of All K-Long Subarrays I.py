class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        l, r = 0, k - 1
        count = collections.Counter(nums[:k])
        
        def xSum(count):
            print(count)
            res = 0
            n = 0
            while n < x:
                if not count: return res
                most_freq = max(count, key=lambda k: (count[k], k))
                res += most_freq * count[most_freq]
                count.pop(most_freq)
                n += 1
            return res

        res.append(xSum(count.copy()))
        while len(res) < len(nums) - k + 1:
            if count[nums[l]] > 1:
                count[nums[l]] -= 1
            else:
                count.pop(nums[l])
            l += 1
            r += 1
            count[nums[r]] = count.get(nums[r], 0) + 1
            res.append(xSum(count.copy()))
        return res

# T: O(n) S: O(n)

