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
	lines = []
	with open("input.txt", 'r') as file_in:
		for line in file_in:
			stripped_line = line.strip()
			line_with_emojis = replace_text_with_emoji(stripped_line)
			lines.append(line_with_emojis)
	return lines

def main():
	lines = read_input_file()
	print(lines)

if __name__ == "__main__":
	main()
