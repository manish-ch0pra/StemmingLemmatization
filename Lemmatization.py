import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["searching", "searched", "searches", "horse", "classifi"]

for word in words:
	print(word, " -> ", lemmatizer.lemmatize(word))
