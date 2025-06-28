from __future__ import annotations
from typing import List, Tuple, Optional, Callable, Iterable
import heapq
import math
import bisect
class LiChaoTree:
    class Line:
        __slots__ = ("a", "b")
        def __init__(self, a: int, b: int):
            self.a = a
            self.b = b
        def eval(self, x: int) -> int:
            return self.a * x + self.b

    def __init__(self, xs: List[int]):
        self.xs = sorted(set(xs))
        self.n = len(self.xs)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        inf = 1 << 60
        self.data = [self.Line(0, inf)] * (2 * self.size)

    def _add_line(self, line: "LiChaoTree.Line", k: int, l: int, r: int):
        mid = (l + r) >> 1
        xl, xm, xr = self.xs[l], self.xs[mid], self.xs[r - 1]
        left_is_better = line.eval(xl) < self.data[k].eval(xl)
        mid_is_better = line.eval(xm) < self.data[k].eval(xm)
        if mid_is_better:
            self.data[k], line = line, self.data[k]
        if r - l == 1:
            return
        if left_is_better != mid_is_better:
            self._add_line(line, k * 2, l, mid)
        else:
            self._add_line(line, k * 2 + 1, mid, r)

    def add_line(self, a: int, b: int):
        self._add_line(self.Line(a, b), 1, 0, self.size)

    def _query(self, x: int, k: int, l: int, r: int) -> int:
        res = self.data[k].eval(x)
        if r - l == 1:
            return res
        mid = (l + r) >> 1
        if x < self.xs[mid]:
            return min(res, self._query(x, k * 2, l, mid))
        else:
            return min(res, self._query(x, k * 2 + 1, mid, r))

    def query(self, x: int) -> int:
        idx = bisect.bisect_left(self.xs, x)
        return self._query(x, 1, 0, self.size)
