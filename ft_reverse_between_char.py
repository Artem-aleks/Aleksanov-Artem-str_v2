def ft_len(a):
    b = 0
    for i in a:
        b += 1
    return b


def ft_find_char(char, f):
    count = 0
    x = 0
    r = 0
    if char in f:
        for i in range(ft_len(f)):
            if str[i] == char:
                x = i
                break
        for i in f:
            if i == char:
                count += 1
        if count == 1:
            return x
        else:
            for i in range(ft_len(f)):
                if f[i] == char:
                    r = i
            return x, r
    else:
        return False


def ft_reverse_str(f):
    a = ''
    for i in range(-1, -ft_len(f) - 1, -1):
        a += f[i]
    return a


def ft_reverse_between_char(char, a):
    b = 0
    for i in a:
        if i == char:
            b += 1
    if b == 0:
        return -2
    elif b == 1:
        return -1
    a, c = ft_find_char(char, a)
    return ft_reverse_str(a[a + 1:c])
