import sys

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

    # print '+++'
    # print sum_list
    # print sum_list[nth_value]
    return sum_list[nth_value]

if __name__ == '__main__':
    # Get the list of input parameters, except for item 0 which is the script name
    arg_list = sys.argv[1:]
    # print arg_list
    sum_series(*arg_list)

    # Fibonacci sequence: first 10 integers
    fibonacci_expected_results_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    # Lucas numbers: first 10 integers
    lucas_expected_results_list = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]

    i = 0
    assert_error = False

    # Loop through values and assert each pair against the correct value from list
    # If a test fails, assign boolean flag

    # Run assert loop for fibonacci
    if arg_list[2] == 0 and arg_list[3] == 1:
        for n in range(10):
            fib_result = fibonacci_expected_results_list[i]
            assert sum_series(n) == fib_result, assert_error == True
            i += 1

    # If there are no errors in the assert run, print success message as per assignment instructions
    if assert_error == False:
        print ('All Fibonacci Tests Pass')