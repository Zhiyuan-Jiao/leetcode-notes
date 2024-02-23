class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

# Iteration:

        if not digits: return []

        digitsMap = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = [i for i in digitsMap[digits[0]]]
        
        for i in digits[1:]:
            newRes = []
            for j in digitsMap[i]:
                for k in res:
                     newRes.append(k + j)
            res = newRes
        return res

# Time complexity: O(n*3^n)
# Space complexity: O(1)

# Backtracking recursion:
        digitsMap = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []

        def backtrack(i, curStr):
            # base case
            if i >= len(digits):
                res.append(curStr)
                return
            
            for c in digitsMap[digits[i]]:
                backtrack(i + 1, curStr + c)

        backtrack(0, "")
        return res if digits else []

# Time complexity: O(n*3^n)
# Space complexity: O(1)