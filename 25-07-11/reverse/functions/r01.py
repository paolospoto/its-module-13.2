def unknown_fn(nums: list[int]) -> list[int]:
    r: list[int] = []
    for n in nums:
        if n % 2 == 0:
            r.append(n ** 2)
    return r


print(unknown_fn([1, 2, 3, 4]))  # ???
