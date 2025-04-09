class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s = s.replace('01', '0 1').replace('10', '1 0').split()
        sl = [len(subs) for subs in s]
        return sum([min(sl[i], sl[i + 1]) for i in range(len(sl) - 1)])