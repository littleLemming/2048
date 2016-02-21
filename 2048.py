import random
import pprint

class Field():

	def __init__(self,size):
		self.field_size = size if size > 2 else 4
		self.field = [[0]*self.field_size for i in range(self.field_size)]

	def get_field(self):
		return self.field

	def get_row(self,row_num):
		if row_num < self.field_size:
			return self.field[row_num]
		return None

	def get_column(self,column_num):
		if column_num < self.field_size:
			column = [0]*self.field_size
			for i in range(self.field_size):
				column[i] = self.field[i][column_num]
			return column
		return None

	def get_value(self,row,column):
		if row < self.field_size and column < self.field_size:
			return self.field[row][column]
		return None

	# should be just used for testing and maybe from inside Field...dunno yet
	def set_value(self,row,column,value):
		if row < self.field_size and column < self.field_size:
			self.field[row][column] = value
			return True
		return False

	def is_full_row(self,row):
		for i in range(self.field_size):
			if field[row][i] == 0:
				return False
		return True

	def is_full_column(self,column):
		for i in range(self.field_size):
			if field[i][column] == 0:
				return False
		return True



	def add_random_number():
		return


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

#print field.pretty_print()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(field.get_field())

field.set_value(1,2,4)
field.set_value(0,2,2)
field.set_value(3,3,2)

pp.pprint(field.get_field())

print field.get_column(2)

#print field.pretty_print()
