import couchdb_map

def testfunc(tweet):
    if tweet["k"]==7:
        #we want to update the document, return true
        tweet["k"]+=1
        tweet["v"]=tweet["k"]+10086
        return True
    else:
        #we don't want to update the document, return false
        return False

def testfunc_new(tweet):
    ret=dict()
    if tweet["k"]<100:
        #we want to update the document, return true
        ret["k"]=tweet['k']+20
        ret['_id']=tweet['_id']
        return ret
    else:
        #we don't want to update the document, return false
        return None

#couchdb_map.map(testfunc,"http://localhost:5984","test")
couchdb_map.map_new(testfunc_new,"http://localhost:5984","test","test_result")