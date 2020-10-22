def ft_len(a):
    s = 0
    for i in a:
        s += 1
    return (s)


def ft_cut_between_char(char, a):
    x = 0
    r = 0
    w = ''
    count = 0
    if char in a:
        for i in a:
            if i == char:
                count += 1

        if count == 1:
            return -1
        else:
            for i in range(ft_len(a)):
                if a[i] == char:
                    x = i

                    break
            for i in range(ft_len(a)):
                if a[i] == char:
                    r = i
            for i in range(x):
                w += a[i]

            r += 1
            while r < ft_len(a):
                w += a[r]
                r += 1
            return w
    else:
        return -2
    
