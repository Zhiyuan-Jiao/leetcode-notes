class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # q = collections.deque()
        # for n in nums:
        #     if n in q:
        #         return True
        #     q.append(n)
        #     if len(q) > k:
        #         q.popleft()
        # return False
        
        # pastNum = dict()
        # for i, n in enumerate(nums):
        #     if n in pastNum and i - pastNum[n] <= k:
        #         return True
        #     pastNum[n] = i
        # return False

        if not k: return False
        pastK = set()
        for i, n in enumerate(nums):
            if n in pastK:
                return True
            if len(pastK) == k:
                pastK.remove(nums[i - k])
            pastK.add(n)
        return False

        T: O(n) S: O(k)