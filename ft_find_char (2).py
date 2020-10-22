def ft_len(sstr):
    l = 0
    for i in sstr:
        l += 1
    return l


def ft_find_char(char, sstr):
    count = 0
    x = 0
    r = 0
    if char in sstr:
        for i in range(ft_len(sstr)):
            if sstr[i] == char:
                x = i
                break
        for i in sstr:
            if i == char:
                count += 1
        if count == 1:
            return x
        else:
            for i in range(ft_len(sstr)):
                if sstr[i] == char:
                    r = i
            return x, r
    else:
        return False
