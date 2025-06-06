class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        path, deadends = set(), set(deadends)

        q = deque()
        q.append(["0000", 0])
        path = set()
        while q:
            cur, moves= q.popleft()
            if cur in path or cur in deadends: continue
            if cur == target:
                return moves
            path.add(cur)
            for i in range(4):
                q.append([cur[:i] + str((int(cur[i]) + 1) % 10) + cur[i + 1:], moves + 1])
                q.append([cur[:i] + str((int(cur[i]) - 1) % 10) + cur[i + 1:], moves + 1])
        return -1