import couchdb
import pickle

'''
map all documents in the db of the url with the map function
Params:
    func: the function to process the documents, the parameter of the func is a dict of a document. The func must
        return True if it wants to update the document
    url: the url of the db
    dbname: the name of the db
    batch_size: the size of one batch of iteration
'''
def map(func,url,dbname,batch_size=5000):
    server = couchdb.Server(url=url)
    db = server[dbname]
    locationDict= {}
    count = 0

    doc_count = db.info()["doc_count"]
    batches = doc_count/batch_size
    if doc_count % batch_size!=0 :
        batches+=1

    for i in range(batches):
        for row in db.view("_all_docs", skip=i*batch_size,limit=batch_size):
            data = db.get(row.id)
            func(data,locationDict)
            count += 1
            if count >= 1000:
                output = open('locationDict.pkl','wb')
                pickle.dump(locationDict,output,protocol=0)
                output.close()
                print("Run successfully")
                exit(0)
        print "Batch", i ,"done"
        

'''
map all documents in the db of the url with the map function, and write to another db
Params:
    func: the function to process the documents, the parameter of the func is a dict of a document. The func should
     return a dict to insert a document or return None
    url: the url of the db
    dbname: the name of the source db
    outdbname: the output db name
    batch_size: the size of one batch of iteration
'''
# def map_new(func,url,dbname,outdbname,batch_size=5000):
#     count = 0
#     server = couchdb.Server(url=url)
#     db = server[dbname]
#     outdb= server[outdbname]

#     doc_count = db.info()["doc_count"]
#     batches = doc_count/batch_size
#     if doc_count % batch_size!=0 :
#         batches+=1

#     for i in range(batches):
#         for row in db.view("_all_docs", skip=i*batch_size,limit=batch_size):
#             data = db.get(row.id)
#             newdata = func(data)
#             outdb.save(newdata)
#             count += 1
#             if count >= 10:
#                 exit(0)
#         print "Batch", i ,"done"
#     