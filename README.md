# AtCoder Utility Library (Python)

KangpingのAtCoder向けライブラリ

競技プログラミング向けに実装した **`atcoder_library.py`** の使い方をまとめたドキュメントです。すべて標準ライブラリのみで動作し、1 ファイルにペーストしてそのまま提出できます。

## 目次

1. [UnionFind (Disjoint‑Set Union)](#1-unionfind-disjoint-set-union)
2. [FenwickTree (Binary Indexed Tree)](#2-fenwicktree-binary-indexed-tree)
3. [SegmentTree](#3-segmenttree)
4. [LazySegMinAdd](#4-lazysegminadd-range-add--range-min)
5. [ModInt & Combination](#5-modint--combination)
6. [Dijkstra](#6-dijkstra)
7. [LCA (Lowest Common Ancestor)](#7-lca-lowest-common-ancestor)
8. [Kosaraju SCC](#8-kosaraju-scc)
9. [Dinic (Maximum Flow)](#9-dinic-maximum-flow)
10. [RollingHash](#10-rollinghash)
11. [LiChaoTree (Convex Hull Trick)](#11-lichaotree-convex-hull-trick)

---

## 使い方

```python
from atcoder_library import *
```

ライブラリはすべて `__all__` に登録済みです。必要なクラス／関数だけを個別インポートしても構いません。

---

## 1. UnionFind (Disjoint‑Set Union)

| 操作            | 計算量         |
| ------------- | ----------- |
| `find(x)`     | α(N) ≈ O(1) |
| `unite(x, y)` | α(N)        |
| `same(x, y)`  | α(N)        |

### 概要

頂点を動的にグループ化し、連結判定や連結成分サイズ取得を高速に行うデータ構造です。経路圧縮とランク併合を実装しています。

### 例

```python
uf = UnionFind(n)
for a, b in edges:
    uf.unite(a, b)
print("Yes" if uf.same(u, v) else "No")
```

---

## 2. FenwickTree (Binary Indexed Tree)

| 操作                 | 計算量      |
| ------------------ | -------- |
| `add(i, x)` (1点加算) | O(log N) |
| `sum(i)` (1〜i 和)   | O(log N) |
| `range_sum(l, r)`  | O(log N) |

### 概要

配列要素の 1 点更新と prefix/区間和を扱います。座標圧縮と組み合わせて出現回数集計、LIS 長さ計算などに便利です。

### 例

```python
bit = FenwickTree(n)
for i, a in enumerate(arr, 1):
    bit.add(i, a)
print(bit.range_sum(l, r))
```

---

## 3. SegmentTree

| 操作             | 計算量      |
| -------------- | -------- |
| `update(i, v)` | O(log N) |
| `query(l, r)`  | O(log N) |

### 概要

関数 `func` が可換・結合的であれば自由に設定できます（`min`, `max`, `sum`, `math.gcd` など）。初期配列は `build()` でまとめて構築可能。

### 例 : 区間最小値

```python
seg = SegmentTree(n, min, float('inf'))
seg.build(initial)
ans = seg.query(l, r)  # [l, r)
```

---

## 4. LazySegMinAdd (Range Add & Range Min)

| 操作                   | 計算量      |
| -------------------- | -------- |
| `range_add(l, r, x)` | O(log N) |
| `range_min(l, r)`    | O(log N) |

### 概要

区間一括加算と区間最小値取得を両立する遅延セグメント木の簡易版です。区間加算・区間最小 DP やスライド最適化で有用です。

### 例

```python
lz = LazySegMinAdd(arr)
lz.range_add(l, r, delta)
print(lz.range_min(0, n))
```

---

## 5. ModInt & Combination

### ModInt

* 四則演算をオーバーロードし `MOD` 自体はグローバルに定義。変更したい場合は `from atcoder_library import MOD; MOD = 998244353` などと上書きしてください。

### Combination

* 前処理 `O(N)`、1 回の nCr 計算 `O(1)`。

```python
MOD = 998244353  # 必要に応じて変更
from atcoder_library import ModInt, Combination
C = Combination(2*10**6)
print(ModInt(C.nCr(n, r)))
```

---

## 6. Dijkstra

非負重みグラフの単一始点最短路。隣接リストは `adj[u] = [(v, w), ...]`。

```python
dist = dijkstra(n, adj, s)
print(dist[t])
```

計算量: `O((V+E) log V)`

---

## 7. LCA (Lowest Common Ancestor)

* 前処理 `O(N log N)`、クエリ `O(log N)`
* `ascend(v, k)` で k 個上の祖先へジャンプ可能。

```python
lca = LCA(n, root, tree)
print(lca.lca(u, v))
```

---

## 8. Kosaraju SCC

強連結成分分解を返す簡潔実装。戻り値は `List[List[int]]` で、各リストが 1 つの SCC。

```python
comps = kosaraju_scc(n, edges)
```

計算量: `O(V + E)`

---

## 9. Dinic (Maximum Flow)

整数容量の最大流アルゴリズム。通常コンテストでは十分高速。

```python
mf = Dinic(n)
for u, v, c in edges:
    mf.add_edge(u, v, c)
print(mf.max_flow(s, t))
```

計算量: `O(E √V)` 程度 (実用的には高速)

---

## 10. RollingHash

二重 Mod のローリングハッシュ。

```python
rh = RollingHash(s)
if rh.get(l1, r1) == rh.get(l2, r2):
    # substrings equal
```

前処理 `O(N)`、クエリ `O(1)`

---

## 11. LiChaoTree (Convex Hull Trick)

動的ラインセット上での最小値クエリ。離散クエリ点集合 `xs` をあらかじめ与えます。

```python
lichao = LiChaoTree(xs)
lichao.add_line(a, b)  # y = ax + b
ans = lichao.query(x)
```

各操作 `O(log N)`

---

## ライセンス

本ライブラリは CC0 (Public Domain) とします。コンテストや学習など、用途を問わず自由に利用・改変してください。
