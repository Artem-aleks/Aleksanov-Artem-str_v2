def ft_len(string):
    count = 0
    for _ in string:
        count += 1
    return count


def ft_find_char(char, string):
    if char not in string:
        return False
    for i in range(ft_len(string)):
        if string[i] == char:
            return i + 1
