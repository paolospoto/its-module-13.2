# def counter(start=0, stop): => buggy
def counter(stop, start=0):
    while start < stop:
        print(start)
        start += 1
