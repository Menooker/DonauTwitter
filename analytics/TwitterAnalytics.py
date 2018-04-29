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

couchdb_map.map(testfunc,"http://localhost:5984","test")