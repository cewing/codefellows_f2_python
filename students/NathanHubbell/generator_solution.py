def intsum():
    num = 0
    count = 1
    while True:
        yield num
        num=num+count
        count+=1


def intsum2():
    num = 0
    count = 1
    while True:
        yield num
        num=num+count
        count+=1


def doubler():
    num=1
    while True:
        yield num
        num=num*2


def fib():
    num=1
    next_num=1
    while True:
        yield num
        num,next_num = next_num,num+next_num


def prime():
    num = [2]
    while True:
        not_prime=0
        for i in num:
            if num[-1]==i:
                yield num[-1]
            elif num[-1]%i==0:
                break
        num.append(num[-1]+1)