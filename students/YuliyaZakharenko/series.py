def fibonacci(n):
	"""return nth value in fibonacci series"""
	if n <= 0:
		print "no value"
	else:
	    series = [0,1]
	    for i in range(2, n):
	        series.append(series[i-1] + series[i-2])
            return series[n-1]


def lucas(n):
	"""return nth value in lucas series"""
	if n <= 0:
		print "no value"
	else:
	    series = [2,1]
	    for i in range(2, n):
	        series.append(series[i-1] + series[i-2])
            return series[n-1]        

def sum_series(n, x = 0, y = 1):
	if x == 0 and y == 1:
		return fibonacci(n)
	elif x == 2 and y == 1:
		return lucas(n)
	else:
	    print "undefined series"	
