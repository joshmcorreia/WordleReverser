from WordleEntry import WordleEntry

def replace_text_with_emoji(input_text: str) -> str:
	"""
	Replaces the input text with an emoji. This may not always be necessary,
	but I've noticed it is necessary when copying/pasting from Slack.

	Ex: `:black_large_square:` -> `⬛`
	"""
	input_text = input_text.replace("⬜", "⬛") # convert light mode to dark mode
	input_text = input_text.replace(":white_large_square:", "⬛") # convert light mode to dark mode
	input_text = input_text.replace(":black_large_square:", "⬛")
	input_text = input_text.replace(":large_yellow_square:", "🟨")
	input_text = input_text.replace(":large_green_square:", "🟩")
	return input_text

def read_input_file():
	"""
	Reads in the input file `input.txt` located in the same folder.
	"""
	wordle_entries = []
	lines = []
	with open("input.txt", 'r') as file_in:
		for line in file_in:
			stripped_line = line.strip()

			if stripped_line == "": # skip blank lines
				continue

			line_with_emojis = replace_text_with_emoji(stripped_line)
			lines.append(line_with_emojis)

			contains_word = any(char.isalpha() for char in line_with_emojis)
			if contains_word:
				wordle_entries.append(lines)
				lines = []
	return wordle_entries

def parse_wordle_entry(wordle_entry: list) -> WordleEntry:
	word_of_the_day = wordle_entry[-1].lower()
	word_of_the_day_letters = list(word_of_the_day)

	wordle_matrix = []
	wordle_entry_rows_only = wordle_entry[:-1] # remove the last entry since that's the word of the day
	for row in wordle_entry_rows_only:
		row_list = list(row)
		wordle_matrix.append(row_list)

	return WordleEntry(word_of_the_day_matrix=word_of_the_day_letters, emoji_matrix=wordle_matrix)

def main():
	wordle_entries = read_input_file()
	all_possible_words = []
	for index, entry in enumerate(wordle_entries):
		wordle_entry = parse_wordle_entry(entry)
		possible_first_words = wordle_entry.possible_first_words
		if index == 0: # populate all_possible_words the first times, and the subsequent times will all be intersections
			all_possible_words = possible_first_words
			continue
		all_possible_words = list(set(all_possible_words) & set(possible_first_words)) # get the intersection between all lists and removes duplicates
	print("It looks like the person who solved these Wordles is using one of the following words:")
	for word in all_possible_words:
		print(word)

if __name__ == "__main__":
	main()
