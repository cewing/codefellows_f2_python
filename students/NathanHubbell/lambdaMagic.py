the_list=[]

[the_list.append(lambda x,e=i: x+e) for i in range(9)] #WHAT!? Why do I need to do the weird e assignmnt?

print the_list[7](8)