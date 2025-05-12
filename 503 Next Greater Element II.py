class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''
        nums = [1, 3, 2, 4]
        res =  [3, 4, 4, -1]

        rearrange nums to make the max number the first
        [1, 4, 2, 3] -> [2, 3, 1, 4]
        use monotonic decreasing stack to get the first larger value from right side
        change res back to the orginal order
        '''
        # 1. rearrange nums to make the max number the first
        maxNum = max(nums)
        maxIdx = nums.index(maxNum)
        nums = nums[maxIdx + 1:] + nums[:maxIdx + 1]
        # print(nums)

        # 2. use monotonic decreasing stack to get the first larger value from right side
        res = [-1] * len(nums)
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            if not stack or n == maxNum:
                stack.append(n)
                continue
            while stack[-1] <= n:
                stack.pop()
            res[i] = stack[-1]
            stack.append(n)
        # print(res)

        # 3. change res back to the orginal order
        return res[-maxIdx - 1:] + res[:-maxIdx - 1]