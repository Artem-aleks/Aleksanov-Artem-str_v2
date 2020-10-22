def ft_len(s):
    r = 0
    for i in s:
        r += 1
    return r


def ft_find_char(char, t):
    count = 0
    x = 0
    r = 0
    if char in t:
        for i in range(ft_len(t)):
            if t[i] == char:
                x = i
                break
        for i in t:
            if i == char:
                count += 1
        if count == 1:
            return x
        else:
            for i in range(ft_len(t)):
                if t[i] == char:
                    r = i
            return x, r
    else:
        return False


def ft_reverse_str(t):
    a = ''
    for i in range(-1, -ft_len(t) - 1, -1):
        a += t[i]
    return a


def ft_reverse_between_char(char, r):
    b = 0
    for i in r:
        if i == char:
            b += 1
    if b == 0:
        return -2
    elif b == 1:
        return -1
    a, c = ft_find_char(char, r)
    return ft_reverse_str(r[a + 1:c])
