import json
from TwitterAPI import TwitterAPI
import TwitterSearch
import TwitterStream

data = json.load(open('config.json'))


consumer_key = data["consumer_key"]
consumer_secret = data["consumer_secret"]
access_token_key = data["access_token_key"]
access_token_secret = data["access_token_secret"]
keywords = data["keywords"]

locations = data['locations']
geocode = data['geocode']


api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token_key,
                 access_token_secret)

#TwitterSearch.search(api,keywords,geocode)
TwitterStream.search(api,keywords,locations)
