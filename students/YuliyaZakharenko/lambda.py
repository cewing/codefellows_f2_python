the_list = []
for n in (range(5)):
    the_list.append(lambda x, y = n: x+y)

the_list = [(lambda x, y=n: x+y) for n in range(5)]



