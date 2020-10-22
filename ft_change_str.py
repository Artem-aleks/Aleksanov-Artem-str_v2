def ft_len(a):
    count = 0
    for _ in a:
        count += 1
    return count


def ft_find_char(b, a):
    if b not in a:
        return False
    for i in range(ft_len(a)):
        if a[i] == b:
            return i


def ft_slice_str(a, start, stop):
    result = ''
    for i in range(start, stop):
        result += a[i]
    return result


def ft_change_str(r, t, y):
    if t not in y:
        return False
    new = ft_slice_str(y, 0, ft_find_char(t[0], y)) \
          + r + ft_slice_str(y, ft_find_char(t[0], y)
                             + ft_len(t), ft_len(y))
    return new
