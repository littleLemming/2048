import random

class Field():

	def __init__(self,size):
		self.field_size = size if size > 2 else 4
		self.field = [[0]*self.field_size]*self.field_size

	def get_column(self,x):
		if x < self.field_size:
			column = [0]*self.field_size
			for i in range(0,self.field_size):
				column[i] = self.field[x][i]
		return None

	def get_row(self,y):
		if y < self.field_size:
			column = [0]*self.field_size
			for i in range(0,self.field_size):
				column[i] = self.field[i][y]
		return None

	def get_value(self,x,y):
		if x < self.field_size and y < self.field_size:
			return self.field[x][y]
		return None

	# should be just used for testing and maybe from inside Field...dunno yet
	def set_value(self,x,y,value):
		if x < self.field_size and y < self.field_size:
			self.field[x][y] = value

	# returns a prettier string-version of the field until the ui is written use this thingie to look at it..
	def pretty_print(self):
		string = ''
		for y in range(0,self.field_size):
			for x in range(0,self.field_size):
				string += '{0} '.format(self.field[x][y])
			string += '\n'
		string = string[:-1]
		return string


class Game():

	# tupel - x,y,value

	def __init__(self,size):
		field = Field(size)
		for i in [1,2]:
			if not self.add_number():
				print 'cannot add {0}'.format(i)
				raise StandardError

	# to be called after the field has been pushed or twice in the very beginning
	# returns True if a number has been added, if not there is no space left - lost
	# TODO check if this method covers all lost cases
	def add_number(self):
		return True

	def sort(self,direction, array):
		return
		#TODO

	# puts arrays into threads to be sorted
	# direction can be 'u', 'd', 'l', 'r'
	def split(self,direction):
		if direction == 'u' or direction == 'd':
			#spalten
			array = sort(direction,array) #in thread

		elif direction == 'l' or direction == 'r':
			#zeilen
			array = sort(direction,array) #in thread


	def move_up(self):
		split('u')

	def move_down(self):
		spilt('d')

	def move_left(self):
		split('l')

	def move_right(self):
		split('r')

###############TESTING###############

# field:
field = Field(4)

print field.pretty_print()
