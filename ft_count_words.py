def ft_count_words(a):
    b = 1
    for i in a:
        if i == ' ':
            b += 1
    return b
