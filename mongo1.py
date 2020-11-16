import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://yohannes:yohannes@cluster0.ehkjm.mongodb.net/student_db?retryWrites=true&w=majority")
#db=client.get_database('sample_airbnb')
print(client.list_database_names())
#records.count_documents({})


#DB_NAME="student_db"

#database=client[DB_NAME]
#print(client.list_database_names())
def checkExistence_DB(db_name,cli):
    dblist=cli.list_database_names()
    if db_name in dblist:
        print(f"DB:'{db_name}' exists")
        return True
    print(f"DB:'{db_name}' not exists or no collection")
    return False

#COLLECTION_NAME="collec1"
#collection=database[COLLECTION_NAME]
def checkExistence_col(COLL,DB_name,db):

    collection_list=db.list_collection_names()
    if COLL in collection_list:
         print(f"collection:'{COLL}' IN DATABASE:'{DB_name}'EXISTS ")
         return True
    print(f"collection:'{COLL}' IN DATABASE:'{DB_name}' not EXISTS ")
    return False
#record={'companyName':'ineuron','product':'affordable ai','courseoffered':'deep learning for computer vision'}
#collection.insert_one(record)
#checkExistence_col(COLLECTION_NAME,DB_NAME,database)
#checkExistence_DB(DB_NAME,client)
list_of_records=[
    {'companyName':'ineuron',
     'product':'affordableai',
     'courseOffered':'Machine Learning With Deployment'},
    {'companyName':'ineuron',
     'prodcut':'affordableai',
     'courseOffered':'Data Science Masters Program'
    },
    {'companyName':'ineuron',
     'product':'Master program',
     'courseOffered':'Data Science Masters Program'
    }
]
#rec=collection.insert_many(list_of_records)
#inserted_ids=rec.inserted_ids
#for idy,uni_id in enumerate(inserted_ids):
#    print(f"{idy}.{uni_id}")
#find_first_record=collection.find_one()
#print(f"the first record of collection: \n{COLLECTION_NAME} is=\n{find_first_record}")
#all_record=collection.find({},{"product"})
#for x,y in enumerate(all_record):
#    print(f"{x}:{y}")
#query={'product':'Master Program'}
#results=collection.find(query)
#for data in results:
#    print(data)
