def frange(start, stop, step=0.25):
    curr = float(start)
    if step != 0:
        while curr < stop:
            yield curr
            curr += step

# Test generator function.
print(list(frange(1.1, 3))) # Should print [1.1, 1.35, 1.6 ..]
print(list(frange(1, 3, 0.33))) # Should print [1.0, 1.33, 1.660000000001..]
print(list(frange(1, 3, 1))) # Should print [1.0, 2.0]
print(list(frange(3, 1))) # Should print an empty list
print(list(frange(1, 3, 0))) # Should print an empty list
print(list(frange(-1, -0.5, 0.1))) # Should print [-1.0, -0.9, -0.8, -0.7000000..]

# Test generator function with iterator for loop.
for num in frange(3.142, 12):
    print(f"{num:05.2f}")
