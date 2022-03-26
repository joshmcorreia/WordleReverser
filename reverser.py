from words import possible_words

def replace_text_with_emoji(input_text):
	"""
	Replaces the input text with an emoji. This may not always be necessary,
	but I've noticed it is necessary when copying/pasting from Slack.

	Ex: `:black_large_square:` -> `⬛`
	"""
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

def main():
	lines = read_input_file()
	print(lines)

if __name__ == "__main__":
	main()
