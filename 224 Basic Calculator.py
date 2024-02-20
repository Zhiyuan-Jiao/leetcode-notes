class Solution:
    def calculate(self, s: str) -> int:
        output, sign, cur, stack = 0, 1, 0, []

        for i in s:
            if i.isdigit():
                cur = cur * 10 + int(i)
            
            # Calculate the output when we are at another operator
            elif i in "+-":
                output += sign * cur
                cur = 0
                sign = -1 if i == "-" else 1

            # Store the previous output and the sign before "(" to a stack to process later
            elif i == "(":
                stack.extend([output, sign])
                # start fresh inside "("
                output, sign = 0, 1

            # Calculate cur as what is inside the "()", retrieve outside output&sign from stack
            elif i == ")":
                output += sign * cur
                cur = output
                sign = stack.pop()
                output = stack.pop()
        return output + sign * cur

# Time complexity: O(n)
# Space complexity: O(1)