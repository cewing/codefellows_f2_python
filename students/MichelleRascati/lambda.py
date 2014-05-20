fun = lambda n: [[lambda x: x + 1] for x in range(n)]

fun = lambda n, x: x + n for x in range(n)

fun = [lambda n: {n: (x + n)} for x in range(n)]

fun = lambda n: [lambda y: y+x for x in range(y)] 

def fun(n):
    f_list = []
    for i in range(n):
        print i
        f_list.append(lambda inp: inp + i)
        print f_list[i](2)
    return f_list
