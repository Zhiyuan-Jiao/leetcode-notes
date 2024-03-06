class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if matrix[mid][0] <= target <= matrix[mid][-1]: # row found
                rl, rr = 0, len(matrix[0])
                while rl <= rr:
                    rmid = (rl + rr) // 2
                    if matrix[mid][rmid] == target: return True
                    elif matrix[mid][rmid] > target: rr = rmid - 1
                    else: rl = rmid + 1
                return False
            elif target > matrix[mid][-1]: l = mid + 1
            else: r = mid - 1
        return False

# Note: double binary search, search for the row then the column
# Time complexity: O(logm + logn)
# Space complexity: O(1)