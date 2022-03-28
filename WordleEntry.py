from words import possible_words

all_letters_list = list("abcdefghijklmnopqrstuvwxyz")

def check_if_word_fits(possible_word: str, row_letter_matrix: list):
	for index, letter in enumerate(possible_word):
		if letter not in row_letter_matrix[index]:
			return False
	return True

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
		for row in self.emoji_matrix:
			for letter_index, emoji in enumerate(row):
				if emoji == "🟩":
					corresponding_letter_of_the_day = [self.word_of_the_day_matrix[letter_index]]
					letter_list.append(corresponding_letter_of_the_day)
				elif emoji == "🟨":
					possible_letters = self.get_list_of_possible_yellow_letters(letter_index)
					letter_list.append(possible_letters)
				else:
					letter_list.append(all_letters_list)
			possible_letter_matrix.append(letter_list)
			letter_list = []
		return possible_letter_matrix

	def find_possible_words(self, row_letter_matrix: list):
		"""
		Builds a list of possible words based on the row_letter_matrix

		Example: if we know the first letter can only be ['n', 'y'], then all words that don't match this are removed from possible_words
		"""
		good_possible_words = []
		for possible_word in possible_words: # loop over each possible word to see if it fits the criteria of the row_letter_matrix
			if check_if_word_fits(possible_word=possible_word, row_letter_matrix=row_letter_matrix) == True:
				good_possible_words.append(possible_word)
		print(good_possible_words)

	def create_letter_matrix(self):
		letter_matrix = []
		possible_letter_matrix = self.get_possible_letter_matrix()
		for row in possible_letter_matrix:
			self.find_possible_words(row)
			print()
		return letter_matrix
