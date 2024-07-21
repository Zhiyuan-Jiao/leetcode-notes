class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x < 10: return True

        cur, temp = 0, x
        while temp:
            digit = temp % 10
            cur = cur * 10 + digit
            temp = temp // 10
        return cur == x

# Note: reverse the entire number and compare
# T: O(n), S: O(1)