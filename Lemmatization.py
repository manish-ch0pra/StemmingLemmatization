import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["grip", "organ", "fast", "horse", "despair"]

for word in words:
	print(word, " -> ", lemmatizer.lemmatize(word))
