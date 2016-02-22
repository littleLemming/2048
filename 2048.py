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
		print "get_value, row: {0}, column: {1}".format(row,column)
		if row < self.field_size and column < self.field_size:
			return self.field[row][column]
		return None

	# should be just used for testing and maybe from inside Field...dunno yet
	def set_value(self,row,column,value):
		print "set_value, row: {0}, column: {1}".format(row,column)
		if row < self.field_size and column < self.field_size:
			self.field[row][column] = value
			return True
		return False

	def is_full_row(self,row):
		print "is_full_row, row: {0}, i's:".format(row)
		for i in range(self.field_size):
			if self.field[row][i] == 0:
				return False
		return True

	def count_empty_row(self,row):
		count = 0
		print "count_empty_row, row: {0}, i's:".format(row)
		for i in range(self.field_size):
			print i
			if self.field[row][i] == 0:
				count += 1
		return count

	def is_full_column(self,column):
		print "is_full_column, column: {0}, i's:".format(column)
		for i in range(self.field_size):
			print i
			if self.field[i][column] == 0:
				return False
		return True

	def count_empty_column(self,column):
		print "count_empty_column: {0}, i's:".format(column)
		count = 0
		for i in range(self.field_size):
			if self.field[i][column] == 0:
				count += 1
		return count
	
	def is_full_spot(self,row,column):
		return not self.field[row][column] == 0

	def is_full_field(self):
		for i in range(self.field_size):
			if not self.is_full_row(i):
				return False
		return True

	def add_random_number(self):
		# TODO: testing. a lot of testing
		# ?optimization? - choose randint from list of already calculated empty rows/columns -> will see how this version does
		if not self.is_full_field():
			row = random.randint(0,self.field_size)
			while self.is_full_row(row):row = random.randint(0,self.field_size)
			column = random.randint(0,self.field_size)
			while self.is_full_spot(row,column):column = random.randint(0,self.field_size)
			value = random.randint(0,2)
			value = 2 if value == 0 or value == 1 else 4 # not yet sure if this would be the right ratio
			self.field[row][column] = value
			return True
		return False


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

for i in range(5):
	field.add_random_number()
	pp.pprint(field.get_field())

#print field.pretty_print()
