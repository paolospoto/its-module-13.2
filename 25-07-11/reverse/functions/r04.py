def unknown_fn(seq: list[int]) -> bool:
    for i in range(1, len(seq)):
        if seq[i] < seq[i - 1]:
            return False
    return True


print(unknown_fn([1, 2, 2, 3]))
print(unknown_fn([3, 1, 4]))
