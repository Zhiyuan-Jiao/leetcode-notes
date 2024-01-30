class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a dict for all the prereq for each course
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # dfs search for the prereq of each crs
        visitSet = set()
        def dfs(crs):
            # loop exist
            if crs in visitSet: return False
            # not prereq or all valid prereq
            if not preMap[crs]: return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

# Algorithm: Use a dict to check if all the prereq are valid for each crs        
# Time complexity: O(n + p)
# Space complexity: O(n)