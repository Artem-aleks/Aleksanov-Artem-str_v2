def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return (a)


def ft_count_words(str):
    k = 0
    d = ft_len(str)
    i = 0
    if str[0] == ' ':
        while i < d:
            if str[i] == ' ' and str[i - 1] != ' ':
                k = k + 1
            i = i + 1
        return k
    else:
        while i < d:
            if str[i] == ' ' and str[i - 1] != ' ':
                k = k + 1
            i = i + 1
        return k + 1
