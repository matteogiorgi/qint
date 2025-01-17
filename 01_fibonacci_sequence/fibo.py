def brute(n: int) -> int:
    if n < 2:
        return 1
    else:
        return brute(n - 1) + brute(n - 2)


def dynamic(n: int, cache: dict[int, int] = {}) -> int:
    if n < 2:
        return 1
    if n not in cache:
        cache[n] = dynamic(n - 1, cache) + dynamic(n - 2, cache)
    return cache[n]
