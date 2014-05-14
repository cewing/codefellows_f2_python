#!/usr/bin/env python


basket = ['Apples', 'Pears', 'Oranges', 'Peaches']


def add_fruit():
	u"""Ask user to add fruit to the list, also insert two list items."""
	
	print basket
	fruit = raw_input(u"What's a fruit you'd like to add to the list?")
	basket.append(fruit)
	print basket
	
	number = raw_input(u'Choose a number')
	fruit_index = basket[int(number) - 1] 
	print number, fruit_index 

	new_basket = ['Plums'] + basket
	print new_basket
	new_basket.insert(0, 'Grapes')
	print new_basket

	for i in new_basket:
		if i[0] == 'P':
			print i

add_fruit()


def remove_fruit():
	u"""Remove last list item and ask user which fruit to remove."""
	
	print basket
	basket.pop()
	print basket
	new_basket = basket * 2

	for i in new_basket[:]:
		bye = raw_input(u'Which fruit would you like to remove?')
		if bye in new_basket:
			new_basket[:] = (i for i in new_basket if i != bye)
		print new_basket
		break 
	
remove_fruit()


def like_dislike():
	u"""For each fruit in the list, modify list based on user input."""
	
	for i in reversed(range(len(basket[:]))):
	    like = raw_input(u'Do you like ' + basket[i].lower()) 
	    if like == u'no':
	    	basket.remove(basket[i])
	    elif like != 'yes':
	    	print u'Please only respond with yes or no'
	print basket
   
like_dislike()


def final():
	u"""Reverse items in the list and delete last item."""
	
	new_basket = [i[::-1] for i in basket]
	basket.pop()
	print basket
	print new_basket

final()

