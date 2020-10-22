def ft_len(a):
    r = 0
    for i in a:
        r += 1
    return r


def ft_find_char(char, a):
    count = 0
    x = 0
    r = 0
    if char in a:
        for i in range(ft_len(a)):
            if a[i] == char:
                x = i
                break
        for i in a:
            if i == char:
                count += 1
        if count == 1:
            return x
        else:
            for i in range(ft_len(a)):
                if a[i] == char:
                    r = i
            return x, r
    else:
        return False
