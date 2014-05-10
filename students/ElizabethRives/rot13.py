


from string import maketrans

def rot13():
	"""Replace each letter in a text by the letter 13 away from it."""

	pass_in = 'abcdefghijklmnopqrstuvwxyz'
	pass_out = 'nopqrstuvwxyzabcdefghijklm'
	table = maketrans(pass_in, pass_out)

	s = "this is a very long string that needs To!"
	


	s_rot13 = s.translate(table)
	print s_rot13

rot13()




	
	







