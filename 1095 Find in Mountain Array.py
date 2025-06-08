# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # binary search peak
        peak = -1
        l, r = 1, mountainArr.length() - 2
        while l <= r:
            m = l + (r - l) // 2
            mid = mountainArr.get(m)
            left, right = mountainArr.get(m - 1), mountainArr.get(m + 1)
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                peak = m
                break
        # print(peak)

        # binary search peak's left side
        res = -1
        l, r = 0, peak
        while l <= r:
            m = l + (r - l) // 2
            midVal = mountainArr.get(m)
            if midVal == target:
                res = m
                break
            elif midVal > target:
                r = m - 1
            else:
                l = m + 1
        
        if res == -1:
            # binary search peak's right side if not in left side
            l, r = peak, mountainArr.length() - 1
            while l <= r:
                m = l + (r - l) // 2
                midVal = mountainArr.get(m)
                if midVal == target:
                    res = m
                    break
                elif midVal > target:
                    l = m + 1
                else:
                    r = m - 1
        return res
        