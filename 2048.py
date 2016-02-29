import random
import pprint

class Field():

	# constructor
	# size: should be lager than 2 - sets the length and width of the field
	def __init__(self,size):
		self.field_size = size if size > 2 else 4
		self.field = [[0]*self.field_size for i in range(self.field_size)]

	# returns the multidimensional array that represents the field
	# should not be used outside of testing
	def get_field(self):
		return self.field

	# returns an array of the row with the row_num
	def get_row(self,row_num):
		if row_num < self.field_size and row_num >= 0:
			return self.field[row_num]
		return None

	# returns an array of the column with the column_num
	def get_column(self,column_num):
		if column_num < self.field_size and column_num >= 0:
			column = [0]*self.field_size
			for i in range(self.field_size):
				column[i] = self.field[i][column_num]
			return column
		return None

	#returns the value of the spot at row/column
	def get_value(self,row,column):
		if row < self.field_size and column < self.field_size:
			return self.field[row][column]
		return None

	# sets the spcified spot at row/column to value
	# should not be used from anywhere except from inside the class 'Field' or for testing
	def set_value(self,row,column,value):
		if row < self.field_size and and row >= 0 column < self.field_size and column >= 0:
			self.field[row][column] = value
			return True
		return False

	# returns True, if the specified row is already full, else False
	# 0 <= row < field_size
	def is_full_row(self,row):
		for i in range(self.field_size):
			if self.field[row][i] == 0:
				return False
		return True

	# returns the amount of empty fields in row
	# 0 <= row < field_size
	def count_empty_row(self,row):
		count = 0
		for i in range(self.field_size):
			if self.field[row][i] == 0:
				count += 1
		return count

	# returns True, if the specified column is already full, else False
	# 0 <= column < field_size
	def is_full_column(self,column):
		for i in range(self.field_size):
			if self.field[i][column] == 0:
				return False
		return True

	# returns the amount of empty fields in column
	# 0 <= column < field_size
	def count_empty_column(self,column):
		count = 0
		for i in range(self.field_size):
			if self.field[i][column] == 0:
				count += 1
		return count
	
	# returns if the spot row/column is already full
	def is_full_spot(self,row,column):
		return not self.field[row][column] == 0

	# returns if there is any empty space
	def is_full_field(self):
		for i in range(self.field_size):
			if not self.is_full_row(i):
				return False
		return True

	# adds in any empty place of the field either a 2 or a 4
	def add_random_number(self):
		if not self.is_full_field():
			row = random.randint(0,self.field_size-1)
			while self.is_full_row(row):row = random.randint(0,self.field_size-1)
			column = random.randint(0,self.field_size-1)
			while self.is_full_spot(row,column):column = random.randint(0,self.field_size-1)
			value = random.randint(0,3)
			value = 2 if value == 0 or value == 1 or value == 2 else 4 # not yet sure if this would be the right ratio
			self.field[row][column] = value
			return True
		return False

	# pushes all of the numbers to eithter the start or end of the array, if there are two spots with the same number 
	# next to each other, irrelevant if there are empyt spots inbetween they get merged into one (the value is double
	# the original value of each of the spots)
	# returns new, sorted array if sorting works, else None
	# TODO: extensive testing
	def resort_array(self,array,direction):
		if direction != 'to_start' and direction != 'to_end':
			return None
		if direction == 'to_end':
			array = reversed(array)
		last = 0
		help_array = [0]*self.field_size
		at = -1
		for i in array:
			if i != 0:
				if at == -1:
					help_array[0] = i
					at = 0
				else:
					if help_array[at] == 0:
						help_array[at] = i
					elif help_array[at] == i:
						help_array[at] = help_array[at]*2
						at += 1
					else:
						at += 1
						help_array[at] = i
		return help_array
		else:
			return None
			

	def push(self, direction):
		if not (direction == 'left' or direction == 'right' or direction == 'up' or direction == 'down'): return
		sort_dir = 'to_start' if direction == 'left' or direction == 'up' else 'to_end'
		for i in range(0,self.field_size-1):
			if direction == 'left' or direction == 'right':
				new_row = self.resort_array(self.get_row(i),sort_dir)
			else:
				new_column = self.resort_array(self.get_column(i)),sort_dir)
			for j in range(0,self.field_size-1):
				if direction == 'left' or direction == 'right':
					self.set_value(i,j,new_row[j])
				else:
					self.set_value(j,i,new_row[j])
					

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

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(field.get_field())

for i in range(17):
	field.add_random_number()
	pp.pprint(field.get_field())
