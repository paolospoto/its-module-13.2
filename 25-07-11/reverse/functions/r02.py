def unknown_fn(nums: list[int]) -> int:
    m = 0
    for n in nums:
        m += n
    return m / len(nums)


print(unknown_fn([5, 7, 9]))
