class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0

        # create adjacency map
        stopToRoute = defaultdict(set)
        for i, route in enumerate(routes): # O(r * s)
            for stop in route:
                stopToRoute[stop].add(i)

        # bfs
        visitedStop, visitedRoute = set([source]), set()
        q = deque()
        for route in stopToRoute[source]: # O(s)
            q.append([route, 1])
            visitedRoute.add(route)
        while q:
            route, buses = q.popleft() # O(r * s)
            for stop in routes[route]:
                if stop == target:
                    return buses
                if stop in visitedStop:
                    continue
                visitedStop.add(stop)
                for nextRoute in stopToRoute[stop]:
                    if nextRoute not in visitedRoute:
                        visitedRoute.add(nextRoute)
                        q.append([nextRoute, buses + 1])
        return -1