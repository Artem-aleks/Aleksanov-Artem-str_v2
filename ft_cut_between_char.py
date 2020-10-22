def ft_count_char_in_str(d, b):
    c = 0
    for i in b:
        if i == d:
            c += 1
    return c


def ft_len(b):
    c = 0
    for _ in b:
        c += 1
    return c


def ft_find_char(d, b):
    if d not in b:
        return False
    for i in range(ft_len(b)):
        if b[i] == d:
            return i + 1


def ft_find_second_char(d, b):
    x = 0
    if ft_count_char_in_str(d, b) == 1:
        return -1
    elif ft_count_char_in_str(d, b) == 0:
        return False
    for i in range(ft_len(b)):
        if b[i] == d:
            x += 1
            if x == 2:
                return i


def ft_slice_str(b, st, sp):
    r = ''
    for i in range(st, sp):
        r += b[i]
    return r


def ft_cut_between_char(d, b):
    if ft_count_char_in_str(d, b) == 1:
        return -1
    elif ft_count_char_in_str(d, b) == 0:
        return -2
    return ft_slice_str(b, 0, ft_find_char(d, b) - 1) + \
        ft_slice_str(b, ft_find_second_char(d, b) + 1, ft_len(b))
