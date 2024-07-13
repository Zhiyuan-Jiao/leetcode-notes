class Solution:
    def intToRoman(self, num: int) -> str:
        # romanTable = [[], ["I", "V"], ["X", "L"], ["C", "D"], ["M"]]
        # res = []
        # digitPlace = 1
        # while num:
        #     subRes = ""

        #     digit = num % 10
        #     if 1 <= digit <= 3:
        #         while digit:
        #             subRes += romanTable[digitPlace][0]
        #             digit -= 1
        #     elif digit == 4:
        #         subRes += "".join(romanTable[digitPlace])
        #     elif digit == 5:
        #         subRes += romanTable[digitPlace][1]
        #     elif 6 <= digit <= 8:
        #         subRes += romanTable[digitPlace][1]
        #         digit -= 5
        #         while digit:
        #             subRes += romanTable[digitPlace][0]
        #             digit -= 1
        #     elif digit == 9:
        #         subRes += romanTable[digitPlace][0] + romanTable[digitPlace + 1][0]

        #     res.append(subRes)
        #     num = num // 10
        #     digitPlace += 1
        # return "".join(res[::-1])

        # Creating Dictionary for Lookup
        num_map = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }
        
        # Result Variable
        r = ''
        
        
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # If n in list then add the roman value to result variable
            while n <= num:
                r += num_map[n]
                num-=n
        return r