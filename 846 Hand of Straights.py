class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        hashMap = Counter(hand)
        minHeap = list(hashMap.keys())
        heapq.heapify(minHeap)
        while minHeap:
            first = minHeap[0]
            for i in range(first, first + groupSize):
                if i not in hashMap: return False
                hashMap[i] -= 1
                if hashMap[i] == 0:
                    if minHeap[0] != i: return False
                    heapq.heappop(minHeap)
        return True
# Algorithm: Greedy
# Note: Use hashmap to track counts, minHeap to track min, since min has to be
# the start of a group whenever we are count a new group
# Time complexity: O(nlogn)
# Space complexity O(n)