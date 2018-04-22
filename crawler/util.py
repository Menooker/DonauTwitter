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