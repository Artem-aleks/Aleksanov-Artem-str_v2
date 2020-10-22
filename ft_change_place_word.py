def ft_len(a):
    d = 0
    for i in a:
        d += 1
    return d


def ft_change_place_word(a):
    i = 0
    s1 = ''
    s2 = ''
    s3 = ''
    while a[i] != ' ':
        s1 += a[i]
        i += 1
    i += 1
    while i < ft_len(a):
        s2 += a[i]
        i += 1
        s3 = s2 + ' ' + s1
    return s3
