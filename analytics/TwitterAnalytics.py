import couchdb_map

def testfunc(tweet):
    tweet["k"]+=1
    tweet["v"]=tweet["k"]+10086

couchdb_map.map(testfunc,"http://localhost:5984","test")