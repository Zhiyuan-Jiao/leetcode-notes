class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        nums1 = [1, 2, 0, 3] -> [1, 2, 1, 3]
        nums2 = [1, 1, 0, 0] -> [1, 1, 2, 3]
        res = 7

        '''
        # get the array with larger sum when replacing all 0s to 1 O(n + m)
        sum1 = 0
        for n in nums1:
            sum1 += n if n != 0 else 1
        sum2 = 0
        for m in nums2:
            sum2 += m if m != 0 else 1
        if sum1 > sum2:
            return sum1 if 0 in nums2 else -1
        elif sum1 < sum2:
            return sum2 if 0 in nums1 else -1
        else:
            return sum1
        # check the array with smaller sum to see if it can reach that sum
        # - has at least one 0
        