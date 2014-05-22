# -*- coding: utf-8 -*-


def count_evens(nums):
	return len([i for i in nums if i%2 == 0])


count_evens([2, 1, 2, 3, 4])
