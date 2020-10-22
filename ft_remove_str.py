def ft_len(string):
    count = 0
    for _ in string:
        count += 1
    return count


def ft_remove_str(str1, str2):
    count = 0
    new_string = str()
    if str2 not in str1:
        return False
    for i in str1:
        if i in str2:
            count += 1
        else:
            new_string += i
    return new_string
