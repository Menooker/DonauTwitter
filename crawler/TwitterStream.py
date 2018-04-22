from TwitterAPI import TwitterAPI
from util import *

def search(api,db,keywords,locations):
    count=0
    query=",".join(keywords)
    r = api.request('statuses/filter', {'locations': locations,'track':query})
    for item in r:
                info = dict()
                info["_id"] = str(item["id"])
                info["user_id"] = item["user"]["id"]
                info["post_text"] = item["text"]
                set_if_not_none(info,"location", get_data(item,["place","name"]) )
                set_if_not_none(info,"location_fullname", get_data(item,["place","full_name"]) )
                c=get_data(item,["place","bounding_box","coordinates"])
                if c:
                    set_if_not_none(info,"coodinates", c[0])
                set_if_not_none(info,"time", get_data(item,["created_at"]))
                count+=1
                #print item["text"]
                if count % 100 ==0:
                    print count