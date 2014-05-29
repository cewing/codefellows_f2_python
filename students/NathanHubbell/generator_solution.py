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
    num = 2
    while True:
        for i in range(2,num+1):
            if num==i:
                yield num
            elif num%i==0:
                break
        num+=1