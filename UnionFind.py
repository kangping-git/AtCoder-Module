from __future__ import annotations
from typing import List, Tuple, Optional, Callable, Iterable
import heapq
import math
import bisect
class UnionFind:
    __slots__ = ("_parent", "_rank", "_size")

    def __init__(self, n: int):
        self._parent = list(range(n))
        self._rank = [0] * n
        self._size = [1] * n

    def find(self, x: int) -> int:
        """Return root of x with path compression."""
        if self._parent[x] != x:
            self._parent[x] = self.find(self._parent[x])
        return self._parent[x]

    def unite(self, x: int, y: int) -> bool:
        """Merge sets. Return True if merged, False if already same."""
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self._rank[x] < self._rank[y]:
            x, y = y, x
        self._parent[y] = x
        self._size[x] += self._size[y]
        if self._rank[x] == self._rank[y]:
            self._rank[x] += 1
        return True

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def size(self, x: int) -> int:
        return self._size[self.find(x)]
