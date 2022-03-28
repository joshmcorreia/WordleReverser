from words import possible_words

class WordleEntry:
	def __init__(self, word_of_the_day_matrix, emoji_matrix):
		self.word_of_the_day_matrix = word_of_the_day_matrix
		self.emoji_matrix = emoji_matrix
		self.entry_matrix = None
		self.letter_matrix = self.create_letter_matrix()

	def get_list_of_possible_yellow_letters(self, index: int) -> list:
		possible_letters = self.word_of_the_day_matrix.copy()
		corresponding_letter = self.word_of_the_day_matrix[index]
		possible_letters.remove(corresponding_letter)
		return possible_letters

	def get_possible_letter_matrix(self) -> list:
		possible_letter_matrix = []
		letter_list = []
		for row_index, row in enumerate(self.emoji_matrix):
			for letter_index, emoji in enumerate(row):
				if emoji == "🟩":
					corresponding_letter_of_the_day = [self.word_of_the_day_matrix[letter_index]]
					letter_list.append(corresponding_letter_of_the_day)
				elif emoji == "🟨":
					possible_letters = self.get_list_of_possible_yellow_letters(letter_index)
					letter_list.append(possible_letters)
				else:
					letter_list.append(None) # In this instance, `None` represents that it can be any letter. This is simpler/prettier than having A-Z
			possible_letter_matrix.append(letter_list)
			letter_list = []
		return possible_letter_matrix

	def create_letter_matrix(self):
		letter_matrix = []
		possible_letter_matrix = self.get_possible_letter_matrix()
		for row in possible_letter_matrix:
			print(row)
		return letter_matrix
