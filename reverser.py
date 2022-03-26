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

def main():
	shared_result = """:black_large_square::black_large_square::black_large_square::black_large_square::large_yellow_square:
:black_large_square::black_large_square::black_large_square::large_yellow_square::black_large_square:
:black_large_square::black_large_square::large_yellow_square::black_large_square::black_large_square:
:large_green_square::black_large_square::black_large_square::large_yellow_square::black_large_square:
:large_green_square::large_green_square::large_green_square::large_green_square::large_green_square:
	"""
	shared_result = replace_text_with_emoji(shared_result)
	print(shared_result)

if __name__ == "__main__":
	main()
