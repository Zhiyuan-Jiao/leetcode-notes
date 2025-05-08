class Solution:
    def racecar(self, target: int) -> int:
        q = deque()
        q.append([0, 1, 0])
        visited = set()

        while q:
            cp, cs, cm = q.popleft()
            if cp == target: return cm

            # avoid revisiting same state
            if (cp, cs) in visited:
                continue

            visited.add((cp, cs))
            q.append([cp + cs, cs * 2, cm + 1])
            if (cs > 0 and cp + cs > target) or (cs < 0 and cp + cs < target):
                q.append([cp, -1 if cs > 0 else 1, cm + 1])
                
