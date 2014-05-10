#!/usr/bin/env python


l = ['Apples', 'Pears', 'Oranges', 'Peaches']


def add_fruit():
	u"""Ask user to add fruit to the list, also insert two list items."""
	
	print l
	fruit = raw_input(u"What's a fruit you'd like to add to the list?")
	l.append(fruit)
	print l
	
	number = raw_input(u'Choose a number')
	fruit_index = l[int(number)] 
	print number, fruit_index 

	new_l = ['Plums'] + l
	print new_l
	new_l.insert(0, 'Grapes')
	print new_l

	for i in new_l:
		if i[0] == 'P':
			print i

add_fruit()


def remove_fruit():
	u"""Remove last list item and ask user which fruit to remove."""
	
	print l
	l.pop()
	print l
	new_l = l * 2

	for i in new_l[:]:
		bye = raw_input(u'Which fruit would you like to remove?')
		if bye in new_l:
			new_l[:] = (i for i in new_l if i != bye)
		print new_l
		break 
	
remove_fruit()


def like_dislike():
	u"""For each fruit in the list, modify list based on user input."""
	
	for i in reversed(range(len(l[:]))):
	    like = raw_input(u'Do you like ' + l[i].lower()) 
	    if like == u'no':
	    	l.remove(l[i])
	    elif like != 'yes':
	    	print u'Please only respond with yes or no'
	print l
   
like_dislike()


def final():
	u"""Reverse items in the list and delete last item."""
	
	new_l = [i[::-1] for i in l]
	l.pop()
	print l
	print new_l

final()

