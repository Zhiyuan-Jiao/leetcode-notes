class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        totalH = sum(damage) + 1
        if armor < max(damage):
            return totalH - armor
        return totalH - max(damage)