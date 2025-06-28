from __future__ import annotations
from typing import List, Tuple, Optional, Callable, Iterable
import heapq
import math
import bisect

class ModInt(int):
    __slots__ = ()

    def __new__(cls, value, mod: int = MOD):
        obj = int.__new__(cls, value % mod)
        obj.mod = mod
        return obj

    def __add__(self, other):
        return ModInt(int(self) + int(other), self.mod)

    __radd__ = __add__

    def __sub__(self, other):
        return ModInt(int(self) - int(other), self.mod)

    def __rsub__(self, other):
        return ModInt(int(other) - int(self), self.mod)

    def __mul__(self, other):
        return ModInt(int(self) * int(other), self.mod)

    __rmul__ = __mul__

    def __pow__(self, power, modulo=None):
        return ModInt(pow(int(self), power, self.mod), self.mod)

    def inv(self):
        return self ** (self.mod - 2)

    def __truediv__(self, other):
        return self * ModInt(other, self.mod).inv()

    def __rtruediv__(self, other):
        return ModInt(other, self.mod) * self.inv()
