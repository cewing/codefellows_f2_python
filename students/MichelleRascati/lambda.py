def fun(n):
    f_list = []
    for i in range(n):
        print i
        f_list.append(lambda inp: inp + i)
        print f_list[i](2)
    return f_list


fun2 = lambda n: [lambda inp: inp + i for i in range(n)]
