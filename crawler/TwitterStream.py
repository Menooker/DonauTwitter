import TwitterAPI
from util import *

def search(api,db,keywords,locations):
    count=0
    query=",".join(keywords)
    
    request_map={'locations': locations}
    if query=="":
        print "empty keywords"
    else:
        request_map['track']=query
    while True:
        try:
            r = api.request('statuses/filter', request_map)
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
        except TwitterAPI.TwitterError.TwitterRequestError as e:
            if e.status_code < 500:
                # something needs to be fixed before re-connecting
                raise
            else:
                # temporary interruption, re-try request
                pass
        except TwitterAPI.TwitterError.TwitterConnectionError:
            # temporary interruption, re-try request
            pass



