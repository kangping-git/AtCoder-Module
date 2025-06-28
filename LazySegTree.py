from __future__ import annotations
from typing import List, Tuple, Optional, Callable, Iterable
import heapq
import math
import bisect

class LazySegMinAdd:
    """Segment tree supporting range add and range minimum query."""

    def __init__(self, arr: List[int]):
        self.n = 1
        while self.n < len(arr):
            self.n <<= 1
        self.dat = [math.inf] * (2 * self.n)
        self.lazy = [0] * (2 * self.n)
        for i, v in enumerate(arr):
            self.dat[self.n + i] = v
        for i in range(self.n - 1, 0, -1):
            self.dat[i] = min(self.dat[2 * i], self.dat[2 * i + 1])

    def _push(self, k: int):
        if self.lazy[k] != 0:
            for c in (2 * k, 2 * k + 1):
                self.dat[c] += self.lazy[k]
                self.lazy[c] += self.lazy[k]
            self.lazy[k] = 0

    def _range_add(self, a: int, b: int, x: int, k: int, l: int, r: int):
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self.dat[k] += x
            self.lazy[k] += x
            return
        self._push(k)
        m = (l + r) >> 1
        self._range_add(a, b, x, 2 * k, l, m)
        self._range_add(a, b, x, 2 * k + 1, m, r)
        self.dat[k] = min(self.dat[2 * k], self.dat[2 * k + 1])

    def range_add(self, l: int, r: int, x: int):
        self._range_add(l, r, x, 1, 0, self.n)

    def _range_min(self, a: int, b: int, k: int, l: int, r: int):
        if b <= l or r <= a:
            return math.inf
        if a <= l and r <= b:
            return self.dat[k]
        self._push(k)
        m = (l + r) >> 1
        return min(self._range_min(a, b, 2 * k, l, m),
                   self._range_min(a, b, 2 * k + 1, m, r))

    def range_min(self, l: int, r: int):
        return self._range_min(l, r, 1, 0, self.n)
