# Enhanced for Production
import decimal

def frange(start, stop=None, step=0.25):
    step = decimal.Decimal(str(step))

    if stop is None:
        stop = decimal.Decimal(str(start))
        curr = decimal.Decimal(0)
    else:
        stop = decimal.Decimal(str(stop))
        curr = decimal.Decimal(str(start))

    if step != 0:
        while curr < stop:
            yield float(curr)
            curr += step

# Test the enhanced frange() function.
print(list(frange(1.1, 3))) # [1.1, 1.35, 1.6, 1.85, 2.1, 2.35, 2.6, 2.85]
print(list(frange(1, 3, 0.33))) # [1.0, 1.33, 1.66, 1.99, 2.32, 2.65, 2.98]
print(list(frange(-1, -0.5, 0.1))) # [-1.0, -0.9, -0.8, -0.7, -0.6]
