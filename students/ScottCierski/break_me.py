# This file contains functions that will deliberately fail

# This function will cause a NameError because x is not defined anywhere
def cause_name_error():
    print(x)

# Useful for running a single function from the command line
if __name__ == '__main__':
    cause_name_error()