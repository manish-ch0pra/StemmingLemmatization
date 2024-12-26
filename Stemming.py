from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["searching", "searched", "searches", "horse"]

for word in words:
	print(word, " -> ", stemmer.stem(word))