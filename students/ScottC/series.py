import sys

# def fibonacci(n):
#     """This function returns the nth value of the Fibonacci sequence"""
#     sum_series(n, 0, 1)

def sum_series(nth_value, first_value = 0, second_value = 1):
    """This function returns the nth value of an integer sequence, wherein each integer is the sum of the previous two."""
    
    # Convert inputs to int
    nth_value = int(nth_value)
    first_value = int(first_value)
    second_value = int(second_value)

    #  Exit if nth_value is negative
    if nth_value < 0:
        print('Only positive values are allowed.')
        return None
    else:
        sum_list = [first_value, second_value]
        print sum_list
        for i in range(nth_value):
            # add current two values, and append sum to end of sum_list
            current_sum = first_value + second_value
            sum_list.append(current_sum)

            # Shift values
            first_value = second_value
            second_value = current_sum

    print '+++'
    print sum_list
    print sum_list[nth_value]
    return sum_list[nth_value]

if __name__ == '__main__':
    # Get the list of input parameters, except for item 0 which is the script name
    print sys.argv[1], sys.argv[2], sys.argv[3]
    sum_series(sys.argv[1], sys.argv[2], sys.argv[3])

    # If inputs for first two sequence values are 0 and 1, test for fibonacci results
    fibonacci_expected_results_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    if int(sys.argv[2]) == 0 and int(sys.argv[3]) == 1:
        i = 0
        for n in range(10):
            fib_result = fibonacci_expected_results_list[i]
            assert sum_series(n) == fib_result
            i += 1

    # If inputs for first two sequence values are 2 and 1, test for lucas results
    lucas_expected_results_list = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]

    if int(sys.argv[2]) == 0 and int(sys.argv[3]) == 1:
        i = 0
        for n in range(10):
            lucas_result = lucas_expected_results_list[i]
            assert sum_series(n) == lucas_result
            i += 1
