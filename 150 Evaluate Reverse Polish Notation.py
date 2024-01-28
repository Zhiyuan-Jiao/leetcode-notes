class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for _ in tokens:
            if _ == "+": stack.append(stack.pop() + stack.pop())
            elif _ == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif _ == "*": stack.append(stack.pop() * stack.pop())
            elif _ == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else: stack.append(int(_))
        return stack[0]

# Algorithm: Use stack to store last two number
# Time complexity: O(n)
# Space complexity: O(n)