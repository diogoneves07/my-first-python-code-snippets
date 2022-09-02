def integers_sum(n):
    try:
        r = sum(range(n+1))
    except TypeError:
        r = 0
    return r


print(integers_sum(10))
