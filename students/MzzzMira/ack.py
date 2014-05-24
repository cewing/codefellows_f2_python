#!/usr/bin/python


def ack(m, n) :
    u""" This function calculates the Ackermann's number 
          m,n          : pozitif integer
          return value : ackermann's value for m,n  
    """
    #type err koyabilirsin
    if m<0 or n<0 :
        #value err koyabilirsin
        return None
    if m==0 :
        return n+1
    if n == 0 :
        return ack(m-1,1)
        
    return ack(m-1, ack(m,n-1))

if __name__ == '__main__':
    u"""test that Ackermann's function performs as expected"""
    ack_test = (
        (-1,  0, None),
        ( 0, -1, None),
        (-1, -1, None),
        (-1,  1, None),
        ( 1, -1, None),
        (0,0,1),
        (0,1,2),
        (0,2,3),
        (0,3,4),
        (0,4,5),
        (1,0,2),
        (1,1,3),
        (1,2,4),
        (1,3,5),
        (1,4,6),
        (2,0,3),
        (2,1,5),
        (2,2,7),
        (2,3,9),
        (2,4,11),
        (3,0,5),
        (3,1,13),
        (3,2,29),
        (3,3,61),
        (3,4,125),
)
    tests_pass = True
    for i,j, expected in ack_test :
        assert ack(i,j) == expected
    else :
        print u"All Tests Pass"

    

#write test code with code. generate the test conditions by coding, nested loop

