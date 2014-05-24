"""List comprehension assignment"""

def count_evens(nums):
    return len([n for n in nums if not n % 2])
