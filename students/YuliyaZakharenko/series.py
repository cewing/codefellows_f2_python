def fibonacci(n):
	"""return nth value in fibonacci series"""
	series = [0,1]
	for i in range(2, n):
	    series.append(series[i-1] + series[i-2])
	    #i = i + 1
        return series[n-1]
