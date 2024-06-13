class Solution:

    # def __init__(self, nums: List[int]):
    #     self.hashMap = collections.defaultdict(list)
    #     for i, n in enumerate(nums):
    #         self.hashMap[n].append(i)

    # def pick(self, target: int) -> int:
    #     return random.choice(self.hashMap[target])
    
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res = -1
        count = 0
        for i, n in enumerate(self.nums):
            if n == target:
                count += 1
                if random.randint(1, count) == count: # if select the count num (1/count chance), replace res with the new idx
                    res = i
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)