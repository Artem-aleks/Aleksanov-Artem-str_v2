def ft_len(stsr):
    m = 0
    for i in stsr:
        m += 1
    return m


def ft_remove_str(str1, str2):
    b = 0
    a = ''
    for i in str1:
        if i in str2:
            b += 1
        else:
            a += i
    if ft_len(str1) == b:
        return False
    else:
        return a
