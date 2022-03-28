import unittest
from reverser import replace_text_with_emoji
from WordleEntry import check_if_word_fits, all_letters_list

class BasicTest(unittest.TestCase):
	def test_replace_text_with_emoji(self):
		input_string = ":black_large_square::black_large_square::black_large_square::black_large_square::large_yellow_square:"
		result = replace_text_with_emoji(input_string)
		expected_output = "⬛⬛⬛⬛🟨"
		self.assertEqual(result, expected_output)

	def test_replace_text_with_emoji_white(self):
		input_string = ":white_large_square::white_large_square::white_large_square::white_large_square::large_yellow_square:"
		result = replace_text_with_emoji(input_string)
		expected_output = "⬛⬛⬛⬛🟨"
		self.assertEqual(result, expected_output)

	def test_replace_text_with_emoji_all_colors(self):
		input_string = ":black_large_square::black_large_square::black_large_square::large_green_square::large_yellow_square:"
		result = replace_text_with_emoji(input_string)
		expected_output = "⬛⬛⬛🟩🟨"
		self.assertEqual(result, expected_output)

	def test_replace_text_with_emojis_already_emojis(self):
		input_string = "⬛⬛⬛🟩🟨"
		result = replace_text_with_emoji(input_string)
		expected_output = "⬛⬛⬛🟩🟨"
		self.assertEqual(result, expected_output)

	def test_replace_text_with_emojis_already_emojis_white(self):
		input_string = "⬜⬜⬜🟩🟨"
		result = replace_text_with_emoji(input_string)
		expected_output = "⬛⬛⬛🟩🟨"
		self.assertEqual(result, expected_output)

	def test_check_if_word_fits(self):
		possible_word = "nubby"
		row_letter_matrix = [['n'], all_letters_list, all_letters_list, all_letters_list, ['n', 'y', 'm', 'p']]
		does_word_fit = check_if_word_fits(possible_word=possible_word, row_letter_matrix=row_letter_matrix)
		self.assertTrue(does_word_fit)

	def test_check_if_word_fits_full_word(self):
		possible_word = "nymph"
		row_letter_matrix = [['n'], ['y'], ['m'], ['p'], ['h']]
		does_word_fit = check_if_word_fits(possible_word=possible_word, row_letter_matrix=row_letter_matrix)
		self.assertTrue(does_word_fit)

	def test_check_if_word_fits_all_letters(self):
		possible_word = "nubby"
		row_letter_matrix = [all_letters_list, all_letters_list, all_letters_list, all_letters_list, all_letters_list]
		does_word_fit = check_if_word_fits(possible_word=possible_word, row_letter_matrix=row_letter_matrix)
		self.assertTrue(does_word_fit)


if __name__ == '__main__':
	unittest.main()
