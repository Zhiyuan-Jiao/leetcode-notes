class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if len(strs) == 1: return strs[0]
        # if strs[0] == "": return ""

        # for i in range(len(strs[0])):
        #     for j in range(1, len(strs)):
        #         if i > len(strs[j]) - 1 or strs[0][i] != strs[j][i]:
        #             return strs[0][:i]
        # return strs[0]
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

# Note: reduce prefix when couldnt find prefix in the cur str
# Time complexity: O(m + n)
# Space complexity: O(1)