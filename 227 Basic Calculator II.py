class Solution:
    def calculate(self, s: str) -> int:
        def helper(sign, v):
            if sign == "+": stack.append(v)
            elif sign == "-": stack.append(-v)
            elif sign == "*": stack.append(stack.pop() * v)
            else: stack.append(int(stack.pop() / v))
        
        stack, num, sign = [], 0, "+"
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == " ": continue
            else:
                helper(sign, num)
                num, sign = 0, c
        helper(sign, num)
        return sum(stack)

# Note: Use stack to track each num and its sign in s, when face "*/", pop to get last val and do the operation
# Time complexity: O(n)
# Space complexity: O(n)