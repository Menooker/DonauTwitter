import couchdb

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
            func(data)
            db.save(data)
        print "Batch", i ,"done"
        