import random
import pprint

class Field():

	# constructor
	# size: should be lager than 2 - sets the length and width of the field
	def __init__(self,size):
		self.field_size = size if size > 2 else 4
		self.field = [[0]*self.field_size for i in range(self.field_size)]
		self.add_random_number()
		self.add_random_number()

	# returns the multidimensional array that represents the field
	def get_field(self):
		return self.field

	# returns an array of the row with the row_num
	def get_row(self,row_num):
		if row_num < self.field_size and row_num >= 0:
			return self.field[row_num]
		return None

	# sets the row at row_num to the row
	def set_row(self,row_num, row):
		if row_num < self.field_size and row_num >= 0 and len(row) == self.field_size:
			self.field[row_num] = row

	# returns an array of the column with the column_num
	def get_column(self,column_num):
		if column_num < self.field_size and column_num >= 0:
			column = [0]*self.field_size
			for i in range(self.field_size):
				column[i] = self.field[i][column_num]
			return column
		return None

	# sets the row at column_num to the column
	def set_column(self,column_num, column):
		if column_num < self.field_size and column_num >= 0 and len(column) == self.field_size:
			self.field[column_num] = column
			for i in range(self.field_size):
				self.field[i][column_num] = column[i]

	#returns the value of the spot at row/column
	def get_value(self,row,column):
		if row < self.field_size and column < self.field_size:
			return self.field[row][column]
		return None

	# sets the spcified spot at row/column to value
	# should not be used from anywhere except from inside the class 'Field' or for testing
	def set_value(self,row,column,value):
		if row < self.field_size and row >= 0 and column < self.field_size and column >= 0:
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

	# return if a push in this direction will do anything - therefor has to be done
	def can_push(self, direction):
		if not (direction == 'left' or direction == 'right' or direction == 'up' or direction == 'down'): return False
		last = -1
		for i in range(0, self.field_size):
			if direction == 'left' or direction == 'right':
				line = list(self.get_row(i))
			else:
				line = list(self.get_column(i))
			if direction == 'right' or direction == 'down':
				line = line[::-1]
			for x in line:
				if last != -1:
					if (last != 0 and x == last) or (last == 0 and x != 0):
						return True
				last = x
			last = -1
		return False
			
	# represents the key-press events in the game
	# calculates the new field
	# TODO
	def push(self, direction):
		if not (direction == 'left' or direction == 'right' or direction == 'up' or direction == 'down'): return False
		"""if not self.can_push(direction):
			print('cannot push')
			return False"""
		print('push: {0}'.format(direction))
		for i in range(0, self.field_size):
			if direction == 'left' or direction == 'right':
				line = list(self.get_row(i))
			else:
				line = list(self.get_column(i))
			if direction == 'right' or direction == 'down':
				line = line[::-1]
		return False



class Game():

	# tupel - x,y,value

	def __init__(self,size):
		field = Field(size)
		for i in [1,2]:
			if not self.add_number():
				print('cannot add {0}'.format(i))
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
dirs = ['up','down','right','left']
pp = pprint.PrettyPrinter(indent=4)

pp.pprint(field.get_field())

for i in dirs:
	field.push(i)
	pp.pprint(field.get_field())

"""for i in range(5):
	field.add_random_number()

pp.pprint(field.get_field())



for i in range(10):
	direction = dirs[random.randint(0,3)]
	print(direction)
	field.push(direction)
	pp.pprint(field.get_field())"""
