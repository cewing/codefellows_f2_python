def get_flower(genus, species, color):
	u"""Returns a NameError"""
	
	print u'Your flower is a %s %s %s.' % (color, genus, species)

get_flower(Rosa, Gallica, red)




def mountain_range():
	u"""Returns a TypeError"""
	
	elevation = raw_input(u"Enter an elevation that's between 8012-8848m")
	s = u'Everest, K2, Kangchenjunga, Lhotse, Makalu, Cho Oyu, Dhaulagiri, Manaslu, Nanga Parbat, Annapurna, Gasherburm I, Broad Peak, Gasherbrum II, Shishapangma'
	if elevation >= 8167:
		del s[7:15]
		return s
	elif elevation < 8167:
		return s[7:15]

mountain_range()

# http://en.wikipedia.org/wiki/List_of_mountains




def create_airports()
	u"""Returns a SyntaxError"""
	
	airports = dict()
	airports[u'Jorge Newbery Airpark'] = u'AEP'
	airports[u'Santos Dumont'] = u'SDU'
	airports[u'Puerto Jimenez'] = u'PJM'
	airports[u'Herrera'] = u'HEX'
	return airports

create_airports()




class Image:
	u"""Returns an AttributeError"""
	
	def __init__(self, ID, width_pixels, height_pixels, total_pixels):
		self.ID = ID
		self.width_pixels = width_pixels
		self.height_pixels = height_pixels
		

cultural_revolution = Image(u'BGE16347', 403, 579, 233337)

print(cultural_revolution.total_pixels)
