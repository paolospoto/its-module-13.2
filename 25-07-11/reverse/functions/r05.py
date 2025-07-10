def unknown_fn(nums: list[int], k: int) -> list[int]:
    r: list[int] = []
    for n in nums:
        if n % k == 0:
            r.append(n)
    return r


print(unknown_fn([2, 3, 4, 6, 7, 9], 3))
