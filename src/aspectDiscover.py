from textblob import TextBlob
from textblob import Word
class AspectDiscover(object):

	def __init__(self, k):
		self.k = k
		self.sentences = []
		self.stopwords = []
		self.wordfrequency = {}
		with open("lemur-stopwords.txt", "r") as stopwordfile:
			for line in stopwordfile:
				self.stopwords.append(line[:-1])
		self.keywords = []
		self.vectors = []
	

	def loadData(self, filename):

		with open(filename, "r") as reviewfile:
			review = TextBlob("")
			for line in reviewfile:
				review += TextBlob(line).lower()
			for sentence in review.sentences:
				tmp = []
				for word in sentence.words:
					if word not in self.stopwords:
						w = Word(word)
						tmp.append(w.lemmatize())
						if word not in self._wordfrequency:
							self.wordfrequency[word] = review.word_counts[word]
				self._sentences.append(tmp)

	def buildVectors(self):
		temp = sorted(self.wordfrequency, key=self.wordfrequency.__getitem__, reverse = True)
		index = 0
		while index < len(temp) and index < 100:
			self.keywords.append(temp[index])
		for sentence in self.sentences:
			vec = []
			for keyword in self.keywords:
				vec.append(sentence.count(keyword))
			self.vectors.append(vec)
		





				




