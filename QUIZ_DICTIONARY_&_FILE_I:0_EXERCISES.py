#MID-SESSION TAKE HOME QUIZ - DICTIONARY & FILE I/0 EXERCISES

#Miranda Remmer
#2.17

import string

MIDSESSION_file = open("midreviewfile.txt")

letters = MIDSESSION_file.read()

MIDSESSION_file.close()

punctuation = string.punctuation
digits = string.digits


def clean_text(file):
	return [letter.strip(punctuation) for word in file for letter in word.split()]

# print clean_text(letters)

def letter_count (file):
	letter_count_dictionary = {}
	file = file.lower() 
	strip = file.strip()
	file_split = clean_text(strip) #unable to strip the extra code
	for letter in file_split:
		if (letter not in punctuation) and (letter not in digits):
			if (letter not in letter_count_dictionary):
				letter_count_dictionary[letter] = 1
			else:
				letter_count_dictionary[letter] += 1
	return letter_count_dictionary


with open("midreviewfile.txt") as MIDSESSION_file:
	midsession_dictionary = letter_count(letters)
	for key, value in sorted(midsession_dictionary.items()):
		print key, ":", value 




