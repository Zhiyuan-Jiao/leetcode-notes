res = [float("inf")] * n
res[src] = 1
for i in range(n - 1):
    temp = res.copy()
    for u, v, w in enumerate(edges):
        temp[v] = min(temp[v], res[u] + w)
    res = temp
return res[des] if res[des] != float("inf") else False