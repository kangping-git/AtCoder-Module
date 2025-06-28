class LCA:
    def __init__(self, n: int, root: int, adj: List[List[int]]):
        self.LOG = (n).bit_length()
        self.parent = [[-1] * n for _ in range(self.LOG)]
        self.depth = [0] * n
        self._dfs(root, -1, 0, adj)
        for k in range(self.LOG - 1):
            for v in range(n):
                p = self.parent[k][v]
                self.parent[k + 1][v] = (-1 if p == -1 else self.parent[k][p])

    def _dfs(self, v: int, p: int, d: int, adj: List[List[int]]):
        self.parent[0][v] = p
        self.depth[v] = d
        for to in adj[v]:
            if to == p:
                continue
            self._dfs(to, v, d + 1, adj)

    def ascend(self, v: int, k: int) -> int:
        for i in range(self.LOG):
            if k >> i & 1:
                v = self.parent[i][v]
                if v == -1:
                    break
        return v

    def lca(self, u: int, v: int) -> int:
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        u = self.ascend(u, self.depth[u] - self.depth[v])
        if u == v:
            return u
        for i in reversed(range(self.LOG)):
            if self.parent[i][u] != self.parent[i][v]:
                u = self.parent[i][u]
                v = self.parent[i][v]
        return self.parent[0][u]
