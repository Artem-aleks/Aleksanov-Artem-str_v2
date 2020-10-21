def ft_len(a):
    b = 0
    for i in a:
        b += 1
    return (b)


def ft_find_second_char(char, a):
    count = 0
    x = 0
    r = 0
    if char in str:
        for i in range(ft_len(a)):
            if str[i] == char:
                x = i

                break

        for i in a:
            if i == char:
                count += 1
        if count == 1:
            return -1
        else:
            for i in range(ft_len(a)):
                if a[i] == char and i != x:
                    r = i

                    break

            return r

    else:
        return -2
