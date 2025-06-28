from __future__ import annotations
from typing import List, Tuple, Optional, Callable, Iterable
import heapq
import math
import bisect

class SegmentTree:
    """Generic segment tree. func must be associative (e.g., min, max, sum)."""

    def __init__(self, n: int, func: Callable, identity):
        self.func = func
        self.identity = identity
        self.size = 1
        while self.size < n:
            self.size <<= 1
        self.data = [identity] * (2 * self.size)

    def build(self, arr: Iterable):
        for i, v in enumerate(arr):
            self.data[self.size + i] = v
        for i in range(self.size - 1, 0, -1):
            self.data[i] = self.func(self.data[2 * i], self.data[2 * i + 1])

    def update(self, idx: int, val):
        idx += self.size
        self.data[idx] = val
        while idx > 1:
            idx >>= 1
            self.data[idx] = self.func(self.data[2 * idx], self.data[2 * idx + 1])

    def query(self, l: int, r: int):
        """Query func over [l, r)"""
        res_left = res_right = self.identity
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                res_left = self.func(res_left, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                res_right = self.func(self.data[r], res_right)
            l >>= 1
            r >>= 1
        return self.func(res_left, res_right)
