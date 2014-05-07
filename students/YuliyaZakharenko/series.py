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
if __name__ == "__main__":
	assert fibonacci(1) == 0
	assert fibonacci(2) == 1
	assert fibonacci(3) == 1
	assert fibonacci(4) == 2
	assert fibonacci(5) == 3
	assert fibonacci(6) == 5
	assert fibonacci(7) == 8
	assert fibonacci(8) == 13
	assert lucas(1) == 2
	assert lucas(2) == 1
	assert lucas(3) == 3
	assert lucas(4) == 4
	assert lucas(5) == 7
	assert lucas(6) == 11
	assert lucas(7) == 18
	assert lucas(8) == 29
