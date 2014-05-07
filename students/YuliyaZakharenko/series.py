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
