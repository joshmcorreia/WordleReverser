from words import possible_words

class WordleEntry:
	def __init__(self, word_of_the_day_matrix, emoji_matrix):
		self.word_of_the_day_matrix = word_of_the_day_matrix
		self.emoji_matrix = emoji_matrix
		self.entry_matrix = None
		self.letter_matrix = self.create_letter_matrix()

	def convert_row_into_letter_list(self, row: list) -> list:
		letter_list = []
		index = 0
		for emoji in row:
			if emoji == "🟩":
				corresponding_letter_of_the_day = self.word_of_the_day_matrix[index]
				letter_list.append(corresponding_letter_of_the_day)
			else:
				letter_list.append(None)
			index += 1
		return letter_list

	def create_letter_matrix(self):
		letter_matrix = []
		for row in self.emoji_matrix:
			letter_list = self.convert_row_into_letter_list(row)
			letter_matrix.append(letter_list)
		return letter_matrix
