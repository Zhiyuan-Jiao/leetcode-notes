class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q, visited, res = deque([s]), set(), s
        while q:
            cur = q.popleft()
            if cur < res:
                res = cur
            visited.add(cur)

            cur_after_a = ""
            for i in range(len(cur)):
                if i % 2:
                    cur_after_a += str((int(cur[i]) + a) % 10)
                else:
                    cur_after_a += cur[i]
            # print(cur_after_a)
            if cur_after_a not in visited: 
                visited.add(cur_after_a)
                q.append(cur_after_a)

            cur_after_b = cur[-b:] + cur[:-b]
            if cur_after_b not in visited: 
                visited.add(cur_after_b)
                q.append(cur_after_b)

        return res