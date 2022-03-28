import unittest
from reverser import replace_text_with_emoji

class BasicTest(unittest.TestCase):
	def test_replace_text_with_emoji(self):
		input_string = ":black_large_square::black_large_square::black_large_square::black_large_square::large_yellow_square:"
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


if __name__ == '__main__':
	unittest.main()
