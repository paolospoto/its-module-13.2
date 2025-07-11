def get_multiples_of_k(nums: list[int], k: int) -> list[int]:
    r = []
    for n in nums:
        if n % k == 0:
            r.append(n)
    return r


print(get_multiples_of_k([2, 3, 4, 6, 7, 9], 3))
