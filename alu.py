def alu(x, y, mode):
    if mode == 0:
        return x
    elif mode == 1:
        return x + y
    elif mode == 2:
        return x & y
    else:
        return ~y
