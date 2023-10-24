def frange(start, stop=None, step=0.25):
    if stop is None:
        stop = start # Only 1 parameter, then make this stop.
        curr = 0.0 # And assign 0.0 to start parameter.
    else:
        curr = float(start)
    if step != 0:
        while curr < stop:
            yield curr
            curr += step

# Test the enhanced frange() function.
params_1 = list(frange(3.5))
params_3 = list(frange(0, 3.5, 0.25))
if params_1 == params_3:
    print("Defaults worked!")
else:
    print("Oops!  Defaults did not work")
    print("one:", params_1)
    print("two:", params_3)

