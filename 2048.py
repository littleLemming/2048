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
	# TODO - testing.
	def can_push(self, direction):
		print('can_push: {0}'.format(direction))
		if not (direction == 'left' or direction == 'right' or direction == 'up' or direction == 'down'): return
		if direction == 'up' or direction == 'left':
			i = 0
			add = 1
		else:
			i = self.field_size-1
			add = -1
		empty = []
		values = {}
		first = True
		print('i\'s:')
		while i >= 0 and i < self.field_size:
			print('i: {0}'.format(i))
			if direction == 'left' or direction == 'right':
				line = self.get_column(i)
			else:
				line = self.get_row(i)
			j = 0
			print('j\'s:')
			while j < self.field_size:
				print('j: {0}'.format(j))
				value = line[j]
				if not first:
					if value == 0:
						if empty.count(j) == 0: empty.append(j)
					else:
						if empty.count(j) != 0 or values[j] == value: 
							print('can_push: True')
							return True
						else:
							values[j] = value
				else:
					if value == 0:
						empty.append(j)
					else:
						values[j] = value
				j += 1
			first = False
			i += add
		print('can_push: False')
		return False



	# pushes all of the numbers to eithter the start or end of the array, if there are two spots with the same number 
	# next to each other, irrelevant if there are empyt spots inbetween they get merged into one (the value is double
	# the original value of each of the spots)
	# returns new, sorted array if sorting works, else None
	# TODO: extensive testing
	def resort_array(self,array,direction):
		print('resort_array array: {0}, direction: {1}'.format(array, direction))
		if direction != 'to_start' and direction != 'to_end':
			return None
		new_array = [0]*self.field_size
		if direction == 'to_start':
			for i in range(0,self.field_size):
				new_array[i] = array[i]
		else:
			j = self.field_size-1
			for i in range(0,self.field_size):
				new_array[i] = array[j]
				j -= 1
		print('possibly reversed array: {0}'.format(new_array))
		last = 0
		help_array = [0]*self.field_size
		at = -1
		for i in new_array:
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
		if direction == 'to_end':
			#new_array = [0]*self.field_size
			j = self.field_size-1
			for i in range(0,self.field_size):
				new_array[i] = help_array[j]
				j -= 1
			print('resorted_array: {0}'.format(new_array))
			return new_array
		print('resorted_array: {0}'.format(help_array))
		return help_array

		
			
	# represents the key-press events in the game
	# calculates the new field
	# TODO fix
	def push(self, direction):
		print('push: {0}'.format(direction))
		if self.can_push(direction):
			if not (direction == 'left' or direction == 'right' or direction == 'up' or direction == 'down'): return
			sort_dir = 'to_start' if direction == 'left' or direction == 'up' else 'to_end'
			for i in range(0,self.field_size):
				if direction == 'left' or direction == 'right':
					new_row = self.resort_array(self.get_row(i),sort_dir)
				else:
					new_column = self.resort_array(self.get_column(i),sort_dir)
				for j in range(0,self.field_size):
					if direction == 'left' or direction == 'right':
						self.set_value(i,j,new_row[j])
					else:
						self.set_value(j,i,new_column[j])
			self.add_random_number()


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
pp = pprint.PrettyPrinter(indent=4)

for i in range(5):
	field.add_random_number()

pp.pprint(field.get_field())

dirs = ['up','down','right','left']

for i in range(10):
	direction = dirs[random.randint(0,3)]
	print(direction)
	field.push(direction)
	pp.pprint(field.get_field())
