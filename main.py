import re

def getFileContent(path_to_file):

	file_contents = ""
 
	try:
		with open(path_to_file, 'r') as f:
				file_contents = f.read()
	except FileNotFoundError:
		print(f"File not found at path: {path_to_file}")
		return ""
	except Exception as e:
		print(f"An error occurred: {e}")
		return ""

	return file_contents

def getWordsFrequency(file_contents):
	frequency_map = {}
	# word_list = file_contents.split()
	word_list = re.findall(r'\b\w+\b', file_contents.lower())
 
	for word in word_list:
		word_lower_cased = word.lower()
  
		frequency_map[word_lower_cased] = frequency_map.get(word_lower_cased, 0) + 1
   
	return frequency_map

def getCharFrequency(file_contents):
	frequency_map = {}

	for char in file_contents:
		if char.isalpha():
			lower_cased_char = char.lower()
			frequency_map[lower_cased_char] = frequency_map.get(lower_cased_char, 0) + 1
   
	return frequency_map

def getWordsCount(file_contents):
	return len(re.findall(r'\b\w+\b', file_contents.lower()))

def sort_on(dict_item):
	return dict_item["num"]

def printReport(file_path, word_count, char_frequency):
	print(f"--- Begin report of {file_path} ---")
	print(f"{word_count} words found in the document\n")

	sorted_char_frequency = sorted(
			[{"char": char, "num": freq} for char, freq in char_frequency.items()],
			key=sort_on,
			reverse=True
	)

	for item in sorted_char_frequency:
			print(f"The '{item['char']}' character was found {item['num']} times")
	
	print(f"--- End report ---")


if __name__ == "__main__":
	path_to_file = "books/Frankenstein.txt"
 
	frankenstein_file_contents = getFileContent(path_to_file)
 
	if frankenstein_file_contents:
		words_count = getWordsCount(frankenstein_file_contents)
		char_frequency = getCharFrequency(frankenstein_file_contents)

		print(f"Words count: {words_count}")
		print(f"Char frequency: {char_frequency}")
		printReport(path_to_file, words_count, char_frequency)

