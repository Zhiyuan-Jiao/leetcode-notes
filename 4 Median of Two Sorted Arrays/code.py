class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            m = l + (r - l) // 2
            n = half - (m + 1) - 1

            # Check index when choose all in A or all in B
            Aleft = A[m] if 0 <= m else float("-inf")
            Aright = A[m + 1] if m + 1 < len(A) else float("inf")
            Bleft = B[n] if 0 <= n else float("-inf")
            Bright = B[n + 1] if n + 1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright: # proper cut position
                if total % 2: # odd length
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = m - 1
            else:
                l = m + 1

# Time complexity: O(logn) n = small num list length
# Space complexity: O(m + n)