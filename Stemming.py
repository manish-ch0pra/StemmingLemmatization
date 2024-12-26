from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["grip", "organ", "fast", "horse", "despair"]

for word in words:
	print(word, " -> ", stemmer.stem(word))