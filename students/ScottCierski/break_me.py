# This file contains functions that will deliberately fail

# This function will cause a NameError because x is not defined anywhere
def cause_name_error():
    print(x)

 # This function will cause a TypeError because it attempts to add two different data types (int and string)
def cause_type_error():
    print 1 + 'I am a string'

# Useful for running a single function from the command line
if __name__ == '__main__':
    cause_type_error()