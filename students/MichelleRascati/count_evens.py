def count_evens(nums):
    return len([num for num in nums if not num % 2])

if __name__ == '__main__':
    assert count_evens([2, 1, 2, 3, 4]) == 3
    assert count_evens([2, 2, 0]) == 3
    assert count_evens([1, 3, 5]) == 0
    print 'All Tests Pass'
