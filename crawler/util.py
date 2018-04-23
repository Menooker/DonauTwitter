def get_data(item,path):
    itr=item
    for idx in path:
        if itr and itr.has_key(idx):
            itr=itr[idx]
        else:
            return None
    return itr

def set_if_not_none(info,key,data):
    if data:
        info[key]=data

def get_dict_object_from_tweet(item):
    info = dict()
    
    if 'id' in item:
        info["_id"] = str(item["id"])
    else:
        return None
    d=get_data(item,["user","id"])
    if d:
        info["user_id"] = d
    else:
        return None

    if 'text' in item:
        info["post_text"] = item['text']
    else:
        return None
    set_if_not_none(info,"location", get_data(item,["place","name"]) )
    set_if_not_none(info,"location_fullname", get_data(item,["place","full_name"]) )
    c=get_data(item,["place","bounding_box","coordinates"])
    if c:
        set_if_not_none(info,"coodinates", c[0])
    set_if_not_none(info,"time", get_data(item,["created_at"]))
    return info