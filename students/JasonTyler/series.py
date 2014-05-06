"""For a code fellows assignment. A bunch of Math."""

def fibonacci(nth):
    """Return the nth value of the Fibonacci series"""
    seed1 = 0
    seed2 = 1
    if nth == 1: return 0
    elif nth == 2: return 1
    else:  
        for _ in range(nth - 1):
            new = seed2 + seed1
            seed2 = seed1
            seed1 = new
    return new        
             
    
