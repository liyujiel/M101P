import bottle
import pymongo

@bottle.route('/')
def index():
    # connect to mongoDB
    connection = pymongo.MongoClient('localhost',27017)

    # attach to test databse
    db = connection.test

    # get handle for names collection
    name = db.names

    # find a single document
    item = name.find_one()

    return '<b>Hello %s!</b>'% item['name']

bottle.run(host='127.0.0.1',port=8082)