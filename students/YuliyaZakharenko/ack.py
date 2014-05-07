def A(m,n):
    """Return a value based on the Ackermann function"""
    if m == 0:
        return n+1
    elif m>0 and n ==0:
        return A(m-1, 1)
    else:
        return A(m-1, A(m,n-1))  
def test_fun():
    if A(0,0) == 1 and A(1,0) == 2 and A(2,0) == 3 and A(3,0) == 5 and A(0,1) == 2 and A(1,1) == 3 and A(2,1) == 5 and A(3,1) == 13 and A(0,2) == 3 and A(1,2) == 4 and A(2,2) == 7 and A(3,2) == 29 and A(0,3) == 4 and A(1,3) == 5 and A(2,3) == 9 and A(3,3) == 61 and A(0,4) == 5 and A(1,4) == 6 and A(2,4) == 11 and A(3,4) == 125:
        print "All Tests Pass"    

if __name__ == "__main__":
    test_fun()