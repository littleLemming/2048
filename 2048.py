import random

class Field():

	def __init__(self,size):
		field_size = size if size > 1 else 4
		field = [[0]*field_size]*field_size

	def get_column(self,x):
		if x < size:
			column = [0]*field_size
			for i in range(0,field_size):
				column[i] = field_size[x][i]
		return None

	def get_row(self,y):
		if y < size:
			column = [0]*field_size
			for i in range(0,field_size):
				column[i] = field_size[i][y]
		return None


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

game = Game(9)
