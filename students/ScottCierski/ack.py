def ack(m, n):
    """This function returns the values for Ackermann's Function"""
    if m < 0 or n < 0:
        print('Only positive values are allowed.')
        return None
    elif m == 0:
        return(n+1)
    elif m > 0 and n == 0:
        return(ack(m-1, 1))
    elif m > 0 and n > 0:
        return(ack(m-1, ack(m, n-1)))

if __name__ == '__main__':

    # List of correct answers for the first 16 Ackermann input value pairs
    ack_list = [1,2,3,4,2,3,4,5,3,5,7,9,5,13,29,61]

    i = 0
    ack_error = False

    # Loop through m and n values, and assert each pair against the correct value from ack_list
    # If a test fails, assign boolean flag
    for m in range(4):
        for n in range(4):
            ack_result = ack_list[i]
            assert ack(m, n) == ack_result, ack_error == True
            # print statements for debugging
            # print i, m, n, ack_result, ack_error
            i += 1

    # If there are no errors in the assert run, print success message as per assignment instructions
    if ack_error == False:
        print u"All Tests Pass"