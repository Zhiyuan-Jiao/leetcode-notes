class Solution:
    def isNumber(self, s: str) -> bool:
        # try:
        #     if s == "inf" or s == "-inf" or s == "+inf" or s =="Infinity" or s == "infinity" or s=="+Infinity" or s == "-Infinity" or s == "+infinity" or s == "-infinity" or s == "nan":
        #         return 0
        #     num = float(s)
        #     return 1
        # except:
        #     return 0

        met_dot = met_e = met_digit = False
        for i, c in enumerate(s.strip()):
            if c in "+-":
                if i > 0 and s[i - 1] not in "Ee":
                    return False
            elif c in "Ee":
                if met_e or not met_digit:
                    return False
                met_e = True
                met_digit = False
            elif c == ".":
                if met_dot or met_e:
                    return False
                met_dot = True
            elif c.isdigit():
                met_digit = True
            else:
                return False
        return met_digit

        # T: O(n) S: O(1)