def ft_len(a):
    b = 0
    for _ in a:
        b += 1
    return b


def ft_find_char(char, a):
    if char not in a:
        return False
    for i in range(ft_len(a)):
        if a[i] == char:
            return i + 1
