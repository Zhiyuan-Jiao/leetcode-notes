class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build adjacency list
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[crs].append(pre)

        # dfs whole graph to build the hashmap map each course to its prereqs
        crsPreMap = defaultdict(set)
        def dfs(crs):
            # nonlocal crsPreMap
            if crs not in crsPreMap:
                for pre in adj[crs]:
                    crsPreMap[crs] |= dfs(pre)
                crsPreMap[crs].add(crs)
            return crsPreMap[crs]

        for i in range(numCourses):
            dfs(i)

        # check for each query
        res = []
        for c1, c2 in queries:
            res.append(c1 in crsPreMap[c2])
        return res

# class Solution:
#     def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
#         adj = defaultdict(list)
#         for prereq, crs in prerequisites:
#             adj[crs].append(prereq)

#         def dfs(crs):
#             if crs not in prereqMap:
#                 prereqMap[crs] = set()
#                 for prereq in adj[crs]:
#                     prereqMap[crs] |= dfs(prereq)
#                 prereqMap[crs].add(crs)
#             return prereqMap[crs]

#         prereqMap = {}
#         for crs in range(numCourses):
#             dfs(crs)

#         res = []
#         for u, v in queries:
#             res.append(u in prereqMap[v])
#         return res