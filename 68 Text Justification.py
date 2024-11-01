class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # if len(words) == 1: return [words[0]]

        res, line, length = [], [], 0
        i = 0
        while i < len(words):
            line.append(words[i])
            length += len(words[i])
            i += 1
            if i < len(words):
                while length <= maxWidth and i < len(words):
                    line.append(" " + words[i])
                    length += len(words[i]) + 1
                    i += 1
                    print(line, length, i)
                if length > maxWidth:
                    i -= 1
                    length -= len(line.pop())

            if len(line) > 1 and i < len(words):
                extraSpace = (maxWidth - length) // (len(line) - 1)
                for j in range(1, len(line)):
                    line[j] = " " * (extraSpace + 1) + line[j] if (maxWidth - length) % (len(line) - 1) >= j else " " * extraSpace + line[j]
            else:
                line[-1] += " " * (maxWidth - length)

            res.append("".join(line))
            line, length = [], 0
        return res

# T: O(n) S: O(n)
                    