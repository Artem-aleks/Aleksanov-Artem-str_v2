def ft_len(a):
    c = 0
    for i in a:
        c += 1
    return (c)


def ft_analysis(a):
    print(a[2])
    print(a[ft_len(a) - 2])
    print(a[0], a[1], a[2], a[3], a[4], sep="")
    i = 0
    while i != ft_len(a) - 2:
        print(a[i], end="")
        i += 1
    i = 0
    print(end="\n")
    while i != ft_len(a):
        if i % 2 == 0:
            print(a[i], end="")
        i += 1
    print(end="\n")
    i = 0
    while i != ft_len(a):
        if i % 2 != 0:
            print(a[i], end="")
        i += 1
    print(end="\n")
    i = 0
    while i != ft_len(a):
        print(a[ft_len(a) - i - 1], end="")
        i += 1
    print(end='\n')
    i = 0
    while i != ft_len(a):
        if i % 2 == 0:
            print(a[ft_len(a) - i - 1], end="")
        i += 1
    print(end='\n')
    print(ft_len(a))
