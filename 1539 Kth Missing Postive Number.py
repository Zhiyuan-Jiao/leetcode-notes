class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # missingCur, missingIdx = 1, 0
        # arrIdx = 0
        # while True:
        #     if missingCur < arr[arrIdx]: 
        #         missingIdx += 1
        #     elif missingCur == arr[arrIdx]:
        #         if arrIdx < len(arr) - 1:
        #             arrIdx += 1
        #     else:
        #         missingIdx += 1

        #     if missingIdx == k:
        #         return missingCur
        #     missingCur += 1

# T: O(n) S: O(1)

        l, r = 0, len(arr) - 1
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] - (m + 1) < k:
                l = m + 1
            else:
                r = m - 1
        return l + k

# T: O(logn) S: O(1)