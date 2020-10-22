def ft_len(str):
    s = 0
    for i in str:
        s += 1
    return (s)


def ft_find_second_char(char, str):
    count = 0
    x = 0
    r = 0
    if char in str:
        for i in range(ft_len(str)):
            if str[i] == char:
                x = i

                break

        for i in str:
            if i == char:
                count += 1
        if count == 1:
            return -1
        else:
            for i in range(ft_len(str)):
                if str[i] == char and i != x:
                    r = i

                    break

            return r
    else:
        return -2
