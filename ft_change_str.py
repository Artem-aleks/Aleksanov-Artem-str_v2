def ft_len(a):
    b = 0
    for i in a:
        b += 1
    return b


def ft_change_str(str1, str2, str3):
    a = ''
    n = 0
    if str3.find(str1) == -1:
        return False
    else:
        while str3.find(str1) != -1:
            n = str3.find(str1)
            a = a + str3[:n] + str2
            str3 = str3[n + ft_len(str1):]
    return a + str3
