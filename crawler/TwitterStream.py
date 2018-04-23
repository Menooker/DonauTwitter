from TwitterAPI import TwitterAPI
from util import *

def search(api,db,keywords,locations):
    count=0
    query=",".join(keywords)
    r = api.request('statuses/filter', {'locations': locations,'track':query})
    for item in r:
                info=get_dict_object_from_tweet(item)
                if not info:
                    print "Error parsing the tweet, ignore it"
                    continue
                db.put(info)
                count+=1
                #print item["text"]
                if count % 200 ==0:
                    print count