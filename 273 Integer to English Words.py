class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"
        threeDigitsNames = ["", "Thousand", "Million", "Billion"]
        digitMap = [
            [90, "Ninety"],
            [80, "Eighty"],
            [70, "Seventy"],
            [60, "Sixty"],
            [50, "Fifty"],
            [40, "Forty"],
            [30, "Thirty"],
            [20, "Twenty"],
            [19, "Nineteen"],
            [18, "Eighteen"],
            [17, "Seventeen"],
            [16, "Sixteen"],
            [15, "Fifteen"],
            [14, "Fourteen"],
            [13, "Thirteen"],
            [12, "Twelve"],
            [11, "Eleven"],
            [10, "Ten"],
            [9, "Nine"],
            [8, "Eight"],
            [7, "Seven"],
            [6, "Six"],
            [5, "Five"],
            [4, "Four"],
            [3, "Three"],
            [2, "Two"],
            [1, "One"]
        ]
        
        def convertToStr(n):
            res = ""
            if n >= 100:
                res += digitMap[-(n // 100)][1] + " Hundred"
                n %= 100
            # print(n)
            while n:
                for d, s in digitMap:
                    if n >= d:
                        n -= d
                        res += " " + s
            return res

        # print(convertToStr(123))
        splitedNums = []
        idx = 0
        while num:
            splitedNums.append(num % 1000)
            num //= 1000
        numStrL = []
        for n in splitedNums:
            numStr = convertToStr(n)
            numStrL.append(numStr)
        res = []
        for i, nStr in enumerate(numStrL):
            if not nStr: continue
            s = nStr + " " + threeDigitsNames[i]
            res.append(s.strip())
        return " ".join(res[::-1]).strip()