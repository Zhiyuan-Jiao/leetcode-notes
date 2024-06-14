class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        prevTime = 0
        stack = []
        res = [0] * n
        for log in logs:
            idx, status, time = log.split(":")
            idx, time = int(idx), int(time)

            if status == "start":
                if stack:
                    res[stack[-1]] += time - prevTime
                prevTime = time
                stack.append(idx)
            else:
                res[stack.pop()] += time - prevTime + 1
                prevTime = time + 1
        
        return res

# Time complexity: O(n)
# Space complexity: O(n)