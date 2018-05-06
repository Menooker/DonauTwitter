import pickle
class Area:
	def __init__(self,name,totalCount,posCount,negCount):
		self.name = name
		self.totalCount = totalCount
		self.posCount = posCount
		self.negCount = negCount
with open('locationDict.pkl', 'rb') as f:
	output = pickle.load(f)
for key,value in output.items():
	print(key,value.totalCount,value.negCount,value.posCount)