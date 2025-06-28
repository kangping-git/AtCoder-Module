def kosaraju_scc(n: int, edges: List[Tuple[int, int]]) -> List[List[int]]:
    g = [[] for _ in range(n)]
    rg = [[] for _ in range(n)]
    for fr, to in edges:
        g[fr].append(to)
        rg[to].append(fr)
    order: List[int] = []
    visited = [False] * n

    def dfs(v: int):
        visited[v] = True
        for nv in g[v]:
            if not visited[nv]:
                dfs(nv)
        order.append(v)

    for v in range(n):
        if not visited[v]:
            dfs(v)

    comp_id = [-1] * n

    def rdfs(v: int, k: int):
        comp_id[v] = k
        for nv in rg[v]:
            if comp_id[nv] == -1:
                rdfs(nv, k)

    k = 0
    for v in reversed(order):
        if comp_id[v] == -1:
            rdfs(v, k)
            k += 1

    comps: List[List[int]] = [[] for _ in range(k)]
    for v, cid in enumerate(comp_id):
        comps[cid].append(v)
    return comps
