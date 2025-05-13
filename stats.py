def get_book_text(path):
        with open(path) as f:
                text = f.read()
                return text

def word_count(path):
        with open(path) as f:
                text = f.read()
                words = len(text.split())
                return f"{words} words found in the document"

def letter_count(path):
	char_count = {}
	with open(path) as f:
		text = f.read()
		text = text.lower()
		for letter in text:
			if letter.isalpha():
				if letter in char_count:
					char_count[letter] += 1
				else:
					char_count[letter] = 1
		return char_count

def book_report(path):
	with open(path) as f:
		text = f.read()
		words = len(text.split())
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}")
	print("----------- Word Count ----------")
	print(f"Found {words} total words")
	print("--------- Character Count -------")
	char = letter_count(path)
	sorted_chars = dict(sorted(char.items(), key=lambda x: x[1], reverse=True))
	for key, value in sorted_chars.items():
		print(f"{key}: {value}")
	return "============= END ==============="
