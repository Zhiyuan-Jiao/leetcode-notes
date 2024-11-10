class Solution:
    def isHappy(self, n: int) -> bool:
        def getDigitSum(n):
            sum = 0
            while n:
                digit = n % 10
                n //= 10
                sum += digit ** 2
            return sum
        
        # visited = set()
        # while n != 1:
        #     n = getDigitSum(n)
        #     if n in visited:
        #         return False
        #     visited.add(n)
        # return True

        slow = fast = n
        while slow != 1 and fast != 1:
            slow = getDigitSum(slow)
            fast = getDigitSum(getDigitSum(fast))
            if slow == fast and slow != 1:
                return False
        return True

# Finding the next value for a given number has a cost of O(logn) because
# we are processing each digit in the number, and the number of digits in a number is given by logn.