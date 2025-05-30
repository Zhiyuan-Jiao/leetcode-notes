class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # build the graph
        graph = [[0] * (query_row + 1) for row in range(query_row + 1)]
        graph[0][0] = poured
        for r in range(query_row + 1):
            for c in range(query_row + 1):
                q = (graph[r][c] - 1) / 2
                if q > 0 and r + 1 <= query_row:
                    graph[r + 1][c] += q
                    graph[r + 1][c + 1] += q
                    graph[r][c] = 1
        print(graph)
        return min(1, graph[query_row][query_glass])