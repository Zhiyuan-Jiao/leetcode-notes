class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        s1 = s2 = maxIdx = len(num) - 1
        for i in range(len(num) - 1, -1, -1):
            if num[i] > num[maxIdx]:
                maxIdx = i
            elif num[i] < num[maxIdx]:
                s1 = i
                s2 = maxIdx
        num[s1], num[s2] = num[s2], num[s1]
        return int("".join(num))

# T: O(n) S: O(n)