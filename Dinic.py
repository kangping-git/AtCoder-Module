class Dinic:
    class Edge:
        __slots__ = ("to", "cap", "rev")
        def __init__(self, to: int, cap: int, rev: int):
            self.to = to
            self.cap = cap
            self.rev = rev

    def __init__(self, n: int):
        self.n = n
        self.graph: List[List[Dinic.Edge]] = [[] for _ in range(n)]

    def add_edge(self, fr: int, to: int, cap: int):
        fwd = Dinic.Edge(to, cap, len(self.graph[to]))
        rev = Dinic.Edge(fr, 0, len(self.graph[fr]))
        self.graph[fr].append(fwd)
        self.graph[to].append(rev)

    def _bfs(self, s: int, t: int, level: List[int]):
        level[:] = [-1] * self.n
        q = [s]
        level[s] = 0
        for v in q:
            for e in self.graph[v]:
                if e.cap and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)

    def _dfs(self, v: int, t: int, f: int, level: List[int], it: List[int]):
        if v == t:
            return f
        for i in range(it[v], len(self.graph[v])):
            e = self.graph[v][i]
            if e.cap and level[v] < level[e.to]:
                d = self._dfs(e.to, t, min(f, e.cap), level, it)
                if d:
                    e.cap -= d
                    self.graph[e.to][e.rev].cap += d
                    return d
            it[v] += 1
        return 0

    def max_flow(self, s: int, t: int) -> int:
        flow = 0
        level = [-1] * self.n
        INF_FLOW = 10 ** 18
        while True:
            self._bfs(s, t, level)
            if level[t] < 0:
                return flow
            it = [0] * self.n
            while True:
                f = self._dfs(s, t, INF_FLOW, level, it)
                if not f:
                    break
                flow += f
