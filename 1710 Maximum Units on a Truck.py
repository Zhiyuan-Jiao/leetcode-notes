class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x : x[1])
        res = 0
        while truckSize > 0 and boxTypes:
            # check have enough for largest box
            if truckSize >= boxTypes[-1][0]:  # if yes, use all
                res += boxTypes[-1][0] * boxTypes[-1][1]
                truckSize -= boxTypes[-1][0]
                boxTypes.pop()
            else:  # if not just use the remaining size, break
                res += truckSize * boxTypes[-1][1]
                break
        return res

        # T:O(nlogn) S:O(1)