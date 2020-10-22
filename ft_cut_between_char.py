def ft_len(str):
    l = 0
    for i in str:
        l += 1
    return (l)


def ft_cut_between_char(char,str):
    x = 0
    r = 0
    w =''
    count = 0
    if char in str:
        for i in str:
            if i == char:
                count+=1

        if count == 1:
            return -1



        else:
            for i in range(ft_len(str)):
                if str[i] == char:
                    x = i

                    break
            for i in range(ft_len(str)):
                if str[i] == char:
                    r = i
            for i in range(x):
                w += str[i]

            r+=1
            while r<ft_len(str):
                w+= str[r]
                r+=1
            return w


    else:
        return -2
print(ft_cut_between_char('3','123456789034563434'))