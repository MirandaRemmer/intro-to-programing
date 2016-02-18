#MID-SESSION TAKE HOME QUIZ - DICTIONARY & FILE I/0 EXERCISES

#Miranda Remmer
#2.17

import string

MIDSESSION_file = open ("midreviewfile2.txt")

words = MIDSESSION_file.read()

MIDSESSION_file.close()

punctuation = string.punctuation
digits = string.digits


def clean_text(file):
	return [word.strip(punctuation) for line in file for word in line.split()]

def word_count (file):
	word_count_dictionary = {}
	file = file.lower()
	file_split = clean_text(file.split())
	for word in file_split:
		if (word not in punctuation) and (word not in digits):  
			if (word not in word_count_dictionary):
				word_count_dictionary[word] = 1
			else:
				word_count_dictionary[word] += 1
	return word_count_dictionary


with open("midreviewfile.txt") as MIDSESSION_file:
	midsession_dictionary = word_count(words)
	for key, value in sorted(midsession_dictionary.items()):
		print key, ":", value 



#maybe add a function to remove certain instances where punctuation within a word exists (e.g. miranda's document - remove ''s')?

