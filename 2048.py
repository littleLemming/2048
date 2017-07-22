import random
import pprint

class Field():

	# constructor
	# size: should be lager than 2 - sets the length and width of the field
	def __init__(self,size):
		self.field_size = size if size >= 3 and size <= 20 else 4
		self.field = [[0]*self.field_size for i in range(self.field_size)]
		self.add_random_number()
		self.add_random_number()
		self.game_over = False
		self.max_num = 0

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
	def push(self, direction):
		if not (direction == 'left' or direction == 'right' or direction == 'up' or direction == 'down'): return False
		print('push: {0}'.format(direction))
		if not self.can_push(direction):
			print('cannot push')
			return False
		for i in range(0, self.field_size):
			last = -1
			if direction == 'left' or direction == 'right':
				line = list(self.get_row(i))
			else:
				line = list(self.get_column(i))
			if direction == 'right' or direction == 'down':
				line = line[::-1]
			new_line = [0]*self.field_size
			spot = 0
			for x in line:
				if spot >= self.field_size:
					raise Exception('push not working', 'serious error in push-method')
				if x != 0:
					if last != -1:
						if x == last:
							new_line[spot] = x**2
							if new_line[spot] > self.max_num:
								self.max_num = new_line[spot]
							last = -1
							spot += 1
						else:
							new_line[spot] = last
							last = x
							spot += 1
					else:
						last = x
			if last != -1 and spot >= self.field_size:
				raise Exception('push not working', 'serious error in push-method')
			if last != -1:
				new_line[spot] = last
			if direction == 'right' or direction == 'down':
				new_line = new_line[::-1]
			if direction == 'left' or direction == 'right':
				self.set_row(i, new_line)
			else:
				self.set_column(i, new_line)
		if not self.add_random_number():
			self.game_over = True
		return True



class Game():

	# constructor
	def __init__(self):
		self.start_game()

	def start_game(self):
		size_s = input("Please enter the size for the game: (minimum is 3, maximum is 20 - if you enter a number out of those bounds the field-size will be 4) ")
		while not size_s.isdigit():
			size_s = input("Please enter a positive integer as the size for the game!")
		self.field = Field(int(size_s))
		print("Field size is: {0}\n".format(self.field.field_size))
		self.print_field()

	def print_field(self):
		print(self.field.field)

	#def play(self):


###############STARTING THE GAME###############

game = Game()

