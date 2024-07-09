class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        for i, c in enumerate(citations):
            count = len(citations) - i
            if c >= count: return count
        return 0

# Note: Iterrate through sorted list to check how many qualified papers left, 
# return qualified papers when it is smaller or equal to the cur paper citations

# T: O(nlogn) S: O(1)