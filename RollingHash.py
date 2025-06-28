class RollingHash:
    _mod1 = 10 ** 9 + 7
    _mod2 = 10 ** 9 + 9
    _base = 911382323  # random odd > alphabet size

    def __init__(self, s: str):
        n = len(s)
        self.pow1 = [1] * (n + 1)
        self.pow2 = [1] * (n + 1)
        for i in range(n):
            self.pow1[i + 1] = self.pow1[i] * self._base % self._mod1
            self.pow2[i + 1] = self.pow2[i] * self._base % self._mod2
        self.h1 = [0] * (n + 1)
        self.h2 = [0] * (n + 1)
        for i, ch in enumerate(s):
            x = ord(ch)
            self.h1[i + 1] = (self.h1[i] * self._base + x) % self._mod1
            self.h2[i + 1] = (self.h2[i] * self._base + x) % self._mod2

    def get(self, l: int, r: int) -> Tuple[int, int]:
        """Return hash of s[l:r]."""
        x1 = (self.h1[r] - self.h1[l] * self.pow1[r - l]) % self._mod1
        x2 = (self.h2[r] - self.h2[l] * self.pow2[r - l]) % self._mod2
        return (x1, x2)
