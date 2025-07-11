def is_in_order(seq: list[int]) -> bool:
    for i in range(1, len(seq)):
        if seq[i] < seq[i - 1]:
            return False
    return True


print(is_in_order([1, 2, 2, 3]))
print(is_in_order([3, 1, 4]))
