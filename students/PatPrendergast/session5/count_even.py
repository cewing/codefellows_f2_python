#count_even.py - done

def count_evens(nums):
    ''' Count the even numbers in a list. '''
    return len([nums for e in nums if e % 2 == 0])

count_evens([2, 1, 2, 3, 4])
count_evens([2, 2, 0])
count_evens([1, 3, 5])