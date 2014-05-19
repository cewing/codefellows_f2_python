# lambda_list.py

def listmaker(n, i=1):
    """ Creates a list of n functions to increment(i) a chosen number (default=1) """
    
    return [lambda e, i=e: e + i for e in range(n)]

'''
    fun_list = []
    for e in range(n):
        print e
        fun_list.append(lambda e, i=e: e + i)
    return fun_list
'''

print '------------'
print listmaker(5)
fun_list = listmaker(10)
print fun_list[3](5)
print '------------'
print fun_list[4](5)
print fun_list[4](9,i=20) 
print '------------'
for e in fun_list:
    print e(5)


