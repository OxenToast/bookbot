from stats import get_book_text
from stats import word_count
from stats import letter_count
from stats import book_report
import sys

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		return sys.exit(1)
	path = sys.argv[1]
	#worded = word_count(path)
	#lettered = letter_count(path)
	#reported = book_report(path)
	print(path) 
	#print(worded) 
	#print(lettered)
	#print(reported)
	print(word_count(path))
	print(letter_count(path))
	print(book_report(path))

main()



#main = book_report("books/frankenstein.txt")
#print(main)
