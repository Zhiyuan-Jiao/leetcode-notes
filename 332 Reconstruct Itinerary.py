class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        tickets.sort()
        for src, des in tickets:
            if src not in adj: adj[src] = []
            adj[src].append(des)
        
        res = ["JFK"]
        def dfs(src):
            # base case
            if len(res) == len(tickets) + 1: return True
            if src not in adj or not adj[src]: return False

            temp = adj[src].copy()
            for i, des in enumerate(temp):
                adj[src].pop(i)
                res.append(des)
                if dfs(des): return True
                adj[src].insert(i, des)
                res.pop()
            return False
        dfs("JFK")
        return res

# Time complexity: O(e^2)
# Space complexity: O(e)