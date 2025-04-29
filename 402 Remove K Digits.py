class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # dp = {} # (i, n) -> smallest pssible integer could get after removing k digits from index i
        # def backtrack(i, n):
        #     # base case
        #     if n == 0:
        #         return num[i:]
        #     if len(num) - i <= n:
        #         return ""
        #     if (i, n) in dp:
        #         return dp[(i, n)]

        #     for j in range(i, len(num)):
        #         # remove current digit
        #             res = backtrack(i + 1, n - 1)
        #         # keep current digit
        #             res = min(res, num[i] + backtrack(i + 1, n))
            
        #     dp[(i, n)] = res
        #     return res

        # res = backtrack(0, k)
        # if not res: return "0"
        # return str(int(res))

        stack = []
        for n in num:
            # keep removing last digit in stack that are larger than cur number
            while k and stack and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)
        if k: stack = stack[:-k]
        # print(stack)
        return "".join(stack).lstrip("0") or "0"

        # numStack = []
        
        # # Construct a monotone increasing sequence of digits
        # for digit in num:
        #     while k and numStack and numStack[-1] > digit:
        #         numStack.pop()
        #         k -= 1
        
        #     numStack.append(digit)
        
        # # - Trunk the remaining K digits at the end
        # # - in the case k==0: return the entire list
        # finalStack = numStack[:-k] if k else numStack
        
        # # trip the leading zeros
        # return "".join(finalStack).lstrip('0') or "0"