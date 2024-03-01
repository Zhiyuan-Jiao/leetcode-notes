class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

# Brute Force
        # if k == 1: return nums

        # inWindow = Counter(nums[0:k])
        # res = [max(nums[0:k])]
        # l, r = 0, k - 1
        # while r < len(nums) - 1:
        #     if inWindow[nums[l]] > 1:
        #         inWindow[nums[l]] -= 1  
        #     else: inWindow.pop(nums[l])
        #     l += 1
        #     r += 1
        #     inWindow[nums[r]] = inWindow.get(nums[r], 0) + 1
        #     res.append(max(inWindow.keys()))
        # return res
# Time complexity: O(n(n - k))
# Space complexity: O(k)

# decreasing queue
        if  k == 1: return nums

        q = collections.deque()
        res = []

        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])

        for j in range(k, len(nums)):
            # pop left when reach max len in queue
            if j - q[0] >= k:
                q.popleft()
            
            # pop right when last num is smaller than cur
            while q and nums[j] >= nums[q[-1]]:
                q.pop()
            q.append(j)

            res.append(nums[q[0]])
        
        return res

# Time complexity: O(n)
# Space complexity: O(k)
            
