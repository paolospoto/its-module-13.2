def unknown_fn(text: str) -> int:
    c = 0
    for ch in text.lower():
        if ch in "aeiou":
            c += 1
    return c


print(unknown_fn("Python"))
