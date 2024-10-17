class Solution:
    def findPermutation(self, s: str) -> List[int]:
        # Initialize an empty stack and a result list
        stack = []
        res = []

        # Append 'I' to the end of the string to handle the last part of the sequence
        s += 'I'

        # Iterate over each character in the modified string
        for i in range(len(s)):
            # Push the current index (1-based) onto the stack
            stack.append(i + 1)

            # When we encounter 'I', pop all elements from the stack and add them to the result
            if s[i] == 'I':
                while stack:
                    res.append(stack.pop())

        # Return the formed permutation
        return res

# T: O(n) S: O(n)
# Greedy