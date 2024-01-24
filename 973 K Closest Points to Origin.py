class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def partition(low, high):
            pivot = points[high][0] ** 2 + points[high][1] ** 2
            i = low
            for j in range(low, high):
                if points[j][0] ** 2 + points[j][1] ** 2 <= pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[high] = points[high], points[i]
            return i
        
        def quickSelect(low, high):
            if low >= high: return
            
            pivot = partition(low, high)
            if pivot == k: return 
            if pivot > k: quickSelect(low, pivot - 1)
            else: quickSelect(pivot + 1, high)

        quickSelect(0, len(points) - 1)
        return points[:k]


Algorithm: quickSelect
Time complecity: O(n) (average), O(n2) (worst)
Space complecity: O(n)