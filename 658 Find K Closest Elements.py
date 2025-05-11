class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # # binary search to find x or cloest value to x in arr
        # l, r = 0, len(arr) - 1
        # x_idx = -1
        # while l <= r:
        #     m = l + (r - l) // 2
        #     print(m)
        #     if arr[m] == x:
        #         x_idx = m
        #         break
        #     elif arr[m] < x:
        #         x_idx = m
        #         l = m + 1
        #     else:
        #         r = m - 1

        # # sliding window to the correct position
        # SWL, SWR = 0, k - 1
        # while SWR + 1 < len(arr) and arr[SWR + 1] - x < x - arr[SWL]:
        #     SWL, SWR = SWL + 1, SWR + 1
        # return arr[SWL : SWR + 1]

        l, r = 0, len(arr) - k - 1
        res = -1
        while l <= r:
            m = l + (r - l) // 2
            print(m)
            if x - arr[m] <= arr[m + k] - x:
                res = m
                r = m - 1
            else:
                l = m + 1
        return arr[res : res + k] if res != -1 else arr[-k:]