class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur = m + n - 1
        m, n = m - 1, n - 1
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[cur] = nums1[m]
                m -= 1
            else:
                nums1[cur] = nums2[n]
                n -= 1
            cur -= 1
        while n >= 0:
            nums1[cur] = nums2[n]
            n -= 1
            cur -= 1

# Time complexity: O(m + n)
# Space complexity: O(1)