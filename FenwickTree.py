from __future__ import annotations
from typing import List, Tuple, Optional, Callable, Iterable
import heapq
import math
import bisect

class FenwickTree:
    __slots__ = ("n", "data")

    def __init__(self, n: int):
        self.n = n
        self.data = [0] * (n + 1)

    def add(self, i: int, x: int):
        """Add x at position i (1-indexed)."""
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def sum(self, i: int) -> int:
        """Prefix sum [1, i] (inclusive)."""
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def range_sum(self, l: int, r: int) -> int:
        """Sum over [l, r] (1-indexed, inclusive)."""
        return self.sum(r) - self.sum(l - 1)
