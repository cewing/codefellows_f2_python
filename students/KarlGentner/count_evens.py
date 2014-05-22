# Returns the count of even numbers in a given list


def count_evens(nums):
    list = [x for x in nums if x % 2 == 0]
    return len(list)