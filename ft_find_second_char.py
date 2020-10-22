def ft_count_char_in_str(char, string):
    count = 0
    for i in string:
        if i == char:
            count += 1
    return count


def ft_len(string):
    count = 0
    for _ in string:
        count += 1
    return count


def ft_find_second_char(char, string):
    cnt = 0
    if ft_count_char_in_str(char, string) == 1:
        return -1
    elif ft_count_char_in_str(char, string) == 0:
        return False
    for i in range(ft_len(string)):
        if string[i] == char:
            cnt += 1
            if cnt == 2:
                return i + 1
