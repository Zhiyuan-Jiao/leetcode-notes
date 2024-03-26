class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            # base case
            if crs in cycle: return False # cycle exist, impossible to finish
            if crs in visit: return True # crs visited before
            
            if preMap[crs]: # prereq exist for this course
                cycle.add(crs)
                for pre in preMap[crs]:
                    if not dfs(pre): return False
                cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        
        for crs in range(numCourses):
            if not dfs(crs): return []
        return output

# Time complexity: O(p + n) P: # of pre, N: # of crs
# Space complexity: O(n)