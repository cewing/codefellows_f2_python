def fun(n):
    f_list = []
    for i in range(n):
        f_list.append(lambda inp, e=i: inp + e)
    return f_list


fun2 = lambda n: [lambda inp, e=i: inp + e for i in range(n)]
