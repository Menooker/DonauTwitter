import pickle
import couchdb_map
from nltk.sentiment.vader import SentimentIntensityAnalyzer
class Area:
	def __init__(self,name,totalCount,posCount,negCount):
		self.name = name
		self.totalCount = totalCount
		self.posCount = posCount
		self.negCount = negCount
		# self.languageDict = languageDict
# with open('output.pkl', 'rb') as f:
# 	output = pickle.load(f)
# locationDict = {}
# for item in output[:1000]:
# 	try:
# 		location = item['location']
# 		if not location in locationDict.keys():
# 			locationDict[location] = Area(name = location, totalCount = 0, posCount = 0, negCount = 0)
# 		locationDict[location].totalCount += 1
# 		sentence = item['post_text']
# 		if sid.polarity_scores(sentence)['neg'] - sid.polarity_scores(sentence)['pos'] > 0:
# 			locationDict[location].negCount += 1
# 		elif sid.polarity_scores(sentence)['neg'] - sid.polarity_scores(sentence)['pos'] < 0:
# 			locationDict[location].posCount += 1
# 	except:
# 		pass
def testfunc(item,locationDict):
	sid = SentimentIntensityAnalyzer()
	try:
		location = item['location']
		if not location in locationDict.keys():
			locationDict[location] = Area(name = location, totalCount = 0, posCount = 0, negCount = 0)
		locationDict[location].totalCount += 1
		sentence = item['post_text']
		if sid.polarity_scores(sentence)['neg'] - sid.polarity_scores(sentence)['pos'] > 0:
			locationDict[location].negCount += 1
		elif sid.polarity_scores(sentence)['neg'] - sid.polarity_scores(sentence)['pos'] < 0:
			locationDict[location].posCount += 1
	except:
		pass
couchdb_map.map(testfunc,"http://localhost:5984","tweets_backup")

