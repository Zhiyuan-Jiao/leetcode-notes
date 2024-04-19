class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet = set()
        while True:
            sumSqr = 0
            while n:
                digit = n % 10
                sumSqr += digit ** 2
                n = n // 10
            if sumSqr == 1: return True
            if sumSqr in hashSet: return False
            hashSet.add(sumSqr)
            n = sumSqr

# Time complexity: O(n) n: # of times of sumSqr to reach sum = 1
# Space complexity: O(n)