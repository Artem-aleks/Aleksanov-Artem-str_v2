def ft_len(a):
    g = 0
    for i in a:
        g += 1
    return g


def ft_remove_str(c, b):
    d = 0
    a = ''
    for i in c:
        if i in b:
            d += 1
        else:
            a += i
    if ft_len(c) == d:
        return False
    else:
        return a
