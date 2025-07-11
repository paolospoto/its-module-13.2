def get_square_of_even_nums(nums: list[int]) -> list[int]:
    even_squared_nums = []
    for n in nums:
        if n % 2 == 0:
            even_squared_nums.append(n ** 2)
    return even_squared_nums


print(get_square_of_even_nums([1, 2, 3, 4]))  # ???
