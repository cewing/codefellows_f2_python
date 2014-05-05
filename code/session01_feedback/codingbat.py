# xyz_there  http://codingbat.com/prob/p149391

# Not bad but maybe a lot of if checking going on
# I do like the return statement though
def xyz_there(string):
    if '.' not in string:
        return ('xyz' in string)
    elif ('.' in string) and ('xyz' in string):
        dotxyzCount = 0
        xyzCount = 0
        for i in range(len(string)):
            if string[i:i+4] == '.xyz':
                dotxyzCount += 1
            if string[i:i+3] == 'xyz':
                xyzCount += 1
    return xyzCount > dotxyzCount

#Kind of hack-y with the replace function to handle the case where 'xyz' and
# '.xyz' appear together I found the approach interesting
def xyz_there(str):
    str = str.replace('.xyz','') #replaces .xyz with space, so one tricky test can pass
    sub_index = str.find('xyz')
  
    return sub_index >= 0 and not str[sub_index-1] == "."

# suggestion
def xyz_there(str):
    return str.count('xyz') > 0 and str.count('xyz') != str.count('.xyz')

# Even better
def xyz_there(str):
    return str.count('xyz') > str.count('.xyz')

# sum13() http://codingbat.com/prob/p167025

# Josh Frailey:
# Has two iterations through the list and one nested iteration through a third created list
# -> Not very O(happy)
def sum13(nums):
    if len(nums) == 0:
        return 0
    else:
        indexOf13s = []
        total = 0
        for i in range(len(nums)):
            if nums[i] == 13:
                indexOf13s.append(i)
                indexOf13s.append(i+1)
        for i in range(len(nums)):
            if i not in indexOf13s:
                total += nums[i]
    return total


# Lack of whitespace reminds me of C, has the fenceposting check of len(nums)
# at the beginning and makes changes to the list in place, which I guess is
# valid but unexpected.
def sum13(nums):
  if len(nums)>0:
    if nums[-1]==13:
      nums[-1]=0
  
  for i in range(len(nums)-1):
    if nums[i]==13:
      nums[i]=0
      nums[i+1]=0
  return sum(nums)


# Obviously the best written code evar
def sum13(nums):
    result, flag = 0, False
    for i in range(len(nums)):
        if nums[i] == 13:
            flag = True
        elif flag and nums[i] != 13:
            flag = False
        else:
            result += nums[i]
    return result


# string_match  http://codingbat.com/prob/p182414

# Nice use of slicing and Python tricks to shorten the code even more than what
# the automatic solution gave
def string_match(a,b):
    count = 0
    for i in range(min([len(a),len(b)])-1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count


# count_hi http://codingbat.com/prob/p167246

# Whitespace aside, I like the use of range and the combined if statement nice
# that for char in range(len(str)-1) can be used as a check against an empty
# string
def count_hi(str):
    count = 0
    for char in range(len(str)-1):
         if str[char] == "h" and str[char+1] == "i":  
              count = count +1
    return count


# end_other  http://codingbat.com/prob/p174314

# Two lines and string methods :)
def end_other(a, b):
    return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())


# Make chocolate  http://codingbat.com/prob/p190859

# Helper functions! Yay!
def make_chocolate(small, big, goal):
     big = trim_big(big, goal)
     bridge = goal - big * 5
     if small >= bridge:
         return bridge
     else:
         return -1
     
def trim_big(big, goal):
    if big * 5 > goal:
        return (goal - (goal % 5))//5
    else:
        return big


# There was a question about the fewest number of lines for make_chocolate()
# so here is Mark's 4 line solution
def make_chocolate(small, big, goal):
    if goal > big * 5 + small or goal % 5 > small:
        return -1
    return goal - (big*5) if goal - (big*5) >= 0 else goal % 5


# and a 2 line solution if a TA really wanted to show off, but that's
# DEFINITELY not my style:
def make_chocolate(small, big, goal):
    return -1 if goal > big * 5 + small or goal % 5 > small else goal - (big*5) if goal - (big*5) >= 0 else goal % 5
