

def count_evens(nums):
    ''' Count the even numbers in a list. '''
    return len([nums for e in nums if e % 2 == 0])

print u'Printing some even numbers out some lists.'
print count_evens([2, 1, 2, 3, 4])
print count_evens([2, 2, 0])
print count_evens([1, 3, 5])

tester = [n for n in range(51)]
print count_evens(tester)