# class Solution:
#     def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
#         pq = [[-l, i] for i, l in enumerate(usageLimits)]
#         heapq.heapify(pq)
#         res = 0
#         while True:
#             waitList = []
#             for j in range(res + 1):
#                 if not pq: return res
#                 l, n = heapq.heappop(pq)
#                 limit = -l
#                 if limit <= 0: return res
#                 limit -= 1
#                 if limit > 0:
#                     waitList.append([-limit, n])
#             for usageLimit in waitList:
#                 heapq.heappush(pq, usageLimit)
#             res += 1
#         return res

class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        print(usageLimits)
    
        total, count = 0, 0
        for i in range(len(usageLimits)):
            total += usageLimits[i]
            if total >= ((count+1)*(count+2))//2:
                count += 1
                
        return count