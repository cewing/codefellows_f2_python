# lambda_list.py

def listmaker(n, i=1):
    """ Creates a list of n functions to increment a chosen number (default=1) """
    
    #return [lambda e, i=1: e + i for e in range(n+1)]

    fun_list = []
    for e in range(n+1):
        print e, i
        fun_list.append(lambda e: e + i)
         # increment up 1... ?
    return fun_list


print listmaker(5)
fun_list = listmaker(10)
print fun_list[3](5)
print '------------'
#print fun_list[4](5)
#print fun_list[4](9,i=20) 

for e in fun_list:
    print e(5)
''' This is currently not adding e and i each time... '''
