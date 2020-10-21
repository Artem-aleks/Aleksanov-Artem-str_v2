def ft_count_char_in_str(b, a):
    count = 0
    for i in a:
        if i == b:
            count += 1
    return count


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
            return i + 1


def ft_find_second_char(b, a):
    c = 0
    if ft_count_char_in_str(b, a) == 1:
        return -1
    elif ft_count_char_in_str(b, a) == 0:
        return False
    for i in range(ft_len(a)):
        if a[i] == b:
            c += 1
            if c == 2:
                return i


def ft_slice_str(a, start, stop):
    result = ''
    for i in range(start, stop):
        result += a[i]
    return result


def ft_cut_between_char(b, a):
    if ft_count_char_in_str(b, a) == 1:
        return -1
    elif ft_count_char_in_str(b, a) == 0:
        return -2
    return ft_slice_str(a, 0, ft_find_char(b, a) - 1) + \
        ft_slice_str(a, ft_find_second_char(b, a) + 1, ft_len(a))
