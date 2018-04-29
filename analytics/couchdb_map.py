import couchdb

'''
map all documents in the db of the url with the map function
Params:
    func: the function to process the documents, the parameter of the func is a dict of a document. The func must
        return True if it wants to update the document
    url: the url of the db
    dbname: the name the db
    batch_size: the size of one batch of iteration
'''
def map(func,url,dbname,batch_size=5000):
    server = couchdb.Server(url=url)
    db = server[dbname]

    doc_count = db.info()["doc_count"]
    batches = doc_count/batch_size
    if doc_count % batch_size!=0 :
        batches+=1

    for i in range(batches):
        for row in db.view("_all_docs", skip=i*batch_size,limit=batch_size):
            data = db.get(row.id)
            if func(data):
                db.save(data)
        print "Batch", i ,"done"
        