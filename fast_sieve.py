def fast_sieve(n: int) -> list[int]:
    """
    n 以下の素数をリストで返す、超高速エラトステネスの篩（ハーフサイズ版）。

    アルゴリズムのポイント:
    - 2 を特別扱いし、以降の奇数のみを bytearray で管理
    - i 番目の要素は「数値 2*i + 1 が素数かどうか」を示す
    - マーク対象は p*p から始め、ステップ幅は p（奇数）に設定
    - スライス代入で一括クリアし、高速化
    """
    if n < 2:
        return []
    # (n>>1) + 1 個の要素を確保: 偶数を除いた奇数だけ
    size = (n >> 1) + 1
    sieve = bytearray(b'\1') * size
    sieve[0] = 0  # 1 は素数扱いしない

    limit = int(n**0.5)
    # i は「値 2*i+1 が候補」のインデックス
    for i in range(1, (limit >> 1) + 1):
        if sieve[i]:
            p = 2*i + 1
            # p*p に対応するインデックス
            start = (p*p) >> 1
            # start から size まで、step=p ずつ False (0) にする
            sieve[start: size: p] = b'\0' * (((size - 1 - start) // p) + 1)

    # 結果を復元: 2 と各奇数を列挙
    primes = [2]
    primes.extend((2*i + 1) for i in range(1, size) if sieve[i])
    return primes
