def ft_len(a):
    d = 0
    for i in a:
        d += 1
    return (d)


def ft_division_str(a):
    if ft_len(a) % 2 == 0:
        i = 0
        s = ''
        n = ''
        q = ''
        while i != ft_len(a) // 2:
            s += a[i]
            i += 1
        while i < ft_len(a):
            n += a[i]
            i += 1
        q = n + s

    else:
        i = 0
        s = ''
        n = ''
        q = ''
        while i != (ft_len(a) + 1) // 2:
            s += a[i]
            i += 1
        while i < ft_len(a):
            n += a[i]
            i += 1
        q = n + s
    return q
