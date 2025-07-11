def get_avg(nums: list[int]) -> int:
    total_sum = 0
    for n in nums:
        total_sum += n
    return total_sum / len(nums)


print(get_avg([5, 7, 9]))
