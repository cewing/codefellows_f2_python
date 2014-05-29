def count_evens(nums):
   even_ints = len([number for number in nums if not number%2])
   return even_ints